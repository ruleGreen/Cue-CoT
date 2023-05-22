import re
import json
import argparse

def save_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def read_jsonl(data_path):
    with open(data_path, "r", encoding="utf-8") as f:
        data = [json.loads(line) for line in f.readlines()]
    return data

def get_machine_scores_from_pairwise_responses(output_path, model_type, dataset, current_number):
    dia_pattern = r"\[Dialogue\](.*?)\[The Start of Response A\]"
    pattern_a = r"\[The Start of Response A\](.*?)\[The End of Response A\]"
    pattern_b = r"\[The Start of Response B\](.*?)\[The End of Response B\]"
    response_eva_raw = read_jsonl(output_path)
    result, number = [], current_number
    for sample in response_eva_raw:
        output = sample["choices"][0]["message"]["content"]
        dialogue = re.findall(dia_pattern, sample["prompt"], flags=re.DOTALL)[0].strip()
        response_a = re.findall(pattern_a, sample["prompt"], flags=re.DOTALL)[0].strip()
        response_b = re.findall(pattern_b, sample["prompt"], flags=re.DOTALL)[0].strip()
        scores = output.split("\n\n")[0]
        comment = output[len(scores):]
        try:
            response_a_score, response_b_score = scores.split(" ")
            ins = {}
            ins["id"] = number
            ins["dataset"] = dataset
            ins["dialogue"] = dialogue
            ins["answers"] = {}
            ins["answers"][model_type] = response_a
            ins["answers"]["ours"] = response_b
            ins["scores"] = {}
            ins["scores"][model_type] = [response_a_score, response_b_score] # 注意，这里score反过来了
            ins["evaluations"] = {}
            ins["evaluations"][model_type] = comment.strip()
            result.append(ins)
            number += 1
        except:
            print("Error")
    return result, number

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--turn_type", type=str, default="multiple", help="the turn type of dialogue including singele or multiple")
    parser.add_argument("--use_desc", type=bool, default=True)
    parser.add_argument("--source_type", type=str, default="status", help="the evidence for response including status, planning and both")
    parser.add_argument("--model_type", type=str, default="chatgpt", help="the models used including chatglm-6b, chatgpt, flan-t5, flan-ul2")
    parser.add_argument("--evaluation_type", type=str, default="helpfulness", help="the evaluation type", choices=["helpfulness", "trustfulness", "acceptness"])
    parser.add_argument("--eval_model_type", type=str, default="chatgpt", help="only use the chatgpt to evaluate")
    parser.add_argument("--eval_data_type", type=str, default="wo_method", help="the compared response cources including w_ground_truth, wo_method")
    parser.add_argument("--setting", type=str, default="zero-shot", help="the settings of the exp including zero-shot and one-shot")
    args = parser.parse_args()

    # init turn_desc / desc / source
    source = "_" + args.source_type
    result_all_mode = []
    current_number = 0
    for dataset_name in ["zhihu", "d4", "quora", "ed", "emh"]:
        turn_desc = ""
        desc = ""
        if dataset_name == "psyqa":
            if args.use_desc:
                desc = "_w_desc"
            else:
                desc = "_wo_desc"
        elif dataset_name == "zhihu":
            if args.turn_type == "single":
                turn_desc = "_single"
            else:
                turn_desc = "_multiple"
    
        output_path = "./dialogue_output/" + args.model_type + "/" + dataset_name + "/dialogue_response_evaluation" + turn_desc + desc + source + "_" + args.setting + "_" + args.evaluation_type + "_" + args.eval_data_type + "_pairwise.json"
        result_each_model, number = get_machine_scores_from_pairwise_responses(output_path, model_type=args.model_type, dataset=dataset_name, current_number=current_number)
        result_all_mode.extend(result_each_model)
        current_number = number

    result = {}
    result["dialogues"] = result_all_mode
    result["models"] = ["chatgpt", "chatglm", "alpaca", "belle", "vicuna"]

    save_json("./web_demo/case_study/data.json", result)