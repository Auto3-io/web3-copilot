from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader, LLMPredictor, ServiceContext
from langchain.chat_models import ChatOpenAI

def search_engine(steps: list[str]):
    index = GPTSimpleVectorIndex.load_from_disk('./index')

    response = index.query(
        "Swap 1000 USDC for ETH on Uniswap.",
        service_context=service_context,
        similarity_top_k=10
    )

    print(response)
