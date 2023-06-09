import os 
from pathlib import Path
from typing import List

from llama_index import (GPTSimpleVectorIndex, LLMPredictor,
                         QuestionAnswerPrompt, ServiceContext)

from copilot.async_util import run_async_tasks
from copilot.config import ChatOpenAI


def search_engine(actions: List[str]):
    p = Path(__file__).with_name('index.json')
    index = GPTSimpleVectorIndex.load_from_disk(p)

    llm_predictor_args = {"temperature":0, "model_name":"gpt-3.5-turbo", "max_tokens":1024}

    if os.getenv('PROMPTLAYER_API_KEY') is not None:
        llm_predictor_args['pl_tags'] = ['search_engine']

    llm_predictor = LLMPredictor(llm=ChatOpenAI(**llm_predictor_args))

    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

    print("start searching: ")

    # define custom QuestionAnswerPrompt
    QA_PROMPT_TMPL = (
        "Write a YAML summary for the action step with a method that is needed to invoke."
        "The summary will help another LLM generate Python program."
        "You should output related usage note, method signature, protocol, contract, chain are required for user to use this method. \n"
        "---------------------\n"
        "{context_str}"
        "\n---------------------\n"
        "Builtin transfer method for ETH: transfer(uint amount, address to)\n"
        "The method name and related information you use must come from the above-mentioned content, "
        "please write summary for action: {query_str}\n\n"
        "You must output the following YAML format. (Replace \" with ` in notes.) \n"
        "Example output 1: \n"
        "methods: \n"
        "  - name: swapMethod(uint amountIn, uint amountOutMin, address[] path, address to, uint deadline) external returns (uint[] amounts)\n"
        "    needed_contracts: (if need address of the contract, you should list them) \n"
        "     - protocol: SomeProtocol (egg., UniswapV2, AaveV2,...)\n"
        "       chain: SomeChain (egg., ethereum, polygon, scroll)\n"
        "       contract: SomeContract (name of the contract, No need to end with a .sol extension.)\n"
        "    notes: \"Some notes to tell user how to use this `swapMethod`, for address [`0x123`, `0x256`].\"\n"
        "Example output 2: \n"
        "methods: \n"
        "  - name: transfer(uint amount, address to)"
        "    needed_contracts: [] (No need to contracts for builtin methods) \n"
        "    notes: \"Some notes to tell user how to use this `transfer`, for address `0x123`.\"\n\n"
        "SUMMARY: \n"
    )
    QA_PROMPT = QuestionAnswerPrompt(QA_PROMPT_TMPL)

    # example_a = "Swap 1 ETH for 1000 USDC on Uniswap."
    # example_b = "Swap 1000 USDC for 1 ETH on Uniswap"
    tasks = [
        index.aquery(action,
                     service_context=service_context,
                     similarity_top_k=5,
                     response_mode="tree_summarize",
                     text_qa_template=QA_PROMPT
                     )
        for action in actions
    ]
    outputs = run_async_tasks(tasks)

    return outputs
