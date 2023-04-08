from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader, LLMPredictor, ServiceContext, QuestionAnswerPrompt
from langchain.chat_models import PromptLayerChatOpenAI
from langchain.callbacks.base import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from copilot.async_util import run_async_tasks

from typing import List


def search_engine(actions: List[str]):
    index = GPTSimpleVectorIndex.load_from_disk('./index.json')

    llm_predictor = LLMPredictor(llm=PromptLayerChatOpenAI(
        temperature=0, model_name="gpt-3.5-turbo", max_tokens=1024, pl_tags=['search_engine']))

    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

    print("start searching: ")

    # define custom QuestionAnswerPrompt
    query_str = "What did the author do growing up?"
    QA_PROMPT_TMPL = (
        "Write a summary for the action step with a method that is needed to invoke."
        "The summary will help another LLM generate Python3 program."
        "You should output related usage note, method signature, protocol, contract, chain are required for user to use this method. \n"
        "---------------------\n"
        "{context_str}"
        "\n---------------------\n"
        "According to above information, please write summary for action: {query_str}\n\n"
        "Example output (You are required to output this format.): \n"
        "- method: swapMethod(uint amountIn, uint amountOutMin, address[] path, address to, uint deadline) external returns (uint[] amounts)\n"
        "  protocol: SomeProtocol (egg., uniswapV2, aavev2,...)\n"
        "  chain: SomeChain (egg., ethereum, polygon, scroll)\n"
        "  contract: SomeContract\n"
        "  notes: Some notes to tell user how to use this method.\n"
    )
    QA_PROMPT = QuestionAnswerPrompt(QA_PROMPT_TMPL)

    # example_a = "Swap 1 ETH for 1000 USDC on Uniswap."
    # example_b = "Swap 1000 USDC for 1 ETH on Uniswap"
    tasks = [
        index.aquery(action,
                     service_context=service_context,
                     similarity_top_k=10,
                     response_mode="tree_summarize",
                     text_qa_template=QA_PROMPT
                     )
        for action in actions
    ]
    outputs = run_async_tasks(tasks)

    return outputs
