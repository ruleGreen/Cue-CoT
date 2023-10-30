<p align="center" width="20%">
<img src="web_demo/assets/claudia.png" alt="CUHK_KFLAB" style="width: 20%; min-width: 30px; display: block; margin: auto;">
</p>

# Cue-CoT: Chain-of-thought Prompting for Responding to In-depth Dialogue Questions with LLMs

[![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg)](https://github.com/tatsu-lab/stanford_alpaca/blob/main/LICENSE)
[![Data License](https://img.shields.io/badge/Data%20License-CC%20By%20NC%204.0-red.svg)](https://github.com/tatsu-lab/stanford_alpaca/blob/main/DATA_LICENSE)

This is the repo for the **CUHK**, **HIT** Dialogue CoT project, which aims to build and share our evaluation benchmarks and our methods to generate personalized, empathetic, and compassionate responses. The repo contains:

- The [3.0K data](#data-release) (500 for each dataset) used for evaluating the model publicly and we save another half of the data for private evaluation.
- The demo for [chatting with the model](#Demo) incorporating our capability. 
- The [case study](#cases) of different datasets.
- The code for [generating the data](#data-generation-process), released soon.
- The code for [evaluating the model](#Evaluation), released soon.


**Note:**
- We will publish cot-tuning model soon. Please stay tuned.
- Usage and License Notices: We use Open AI API to generate some part of our evaluation data. The datasets should not be used outside of research purposes.
- The part of constructed datasets are based on several existing research works. Please cite them and following their used policy if you used corresponding evaluation data.
- We would not release our evaluation data based on PsyQA, adhering to the private policy of the original paper. However, if you have access to the PsyQA, the evaluation data could be automatically constructed by our provided scripts [here](./benchmark/get_preprocessed_data.ipynb).

# Method

<img width="1165" alt="image" src="https://github.com/ruleGreen/Cue-CoT/assets/26263128/f3fb84c5-403a-4544-8e19-314b2caab7b5">


# Global Positions of Current LLMs

<img width="569" alt="image" src="https://github.com/ruleGreen/Cue-CoT/assets/26263128/8bcb3a53-ae2e-4549-8636-26da4857d22e">


# Demo

```
Step1: put your OpenAI Key in web_demo/config.json
Step2: directly run the command: python web_demo/web.py
```

# Cases

```
Pls use browser to open web_demo/index.html
```

# Acknowledgement
```
We want to thank all realted open-source projects, especially but not limited to the following:
https://github.com/LianjiaTech/BELLE/
https://github.com/THUDM/ChatGLM-6B
https://github.com/kaixindelele/ChatPaper and
https://github.com/lm-sys/FastChat/ 
...
```


# Citations

```
@misc{wang2023cuecot,
      title={Cue-CoT: Chain-of-thought Prompting for Responding to In-depth Dialogue Questions with LLMs}, 
      author={Hongru Wang and Rui Wang and Fei Mi and Yang Deng and Zezhong Wang and Bin Liang and Ruifeng Xu and Kam-Fai Wong},
      year={2023},
      eprint={2305.11792},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
