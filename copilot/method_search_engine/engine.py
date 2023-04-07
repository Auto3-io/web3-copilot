from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader, LLMPredictor, ServiceContext
from langchain.chat_models import ChatOpenAI

def search_engine(steps: list[str]):
    results = []
    for step in steps:
        documents = SimpleDirectoryReader('data').load_data()
        llm_predictor = LLMPredictor(llm=ChatOpenAI(
            temperature=0, model_name="gpt-3.5-turbo"))
        service_context = ServiceContext.from_defaults(
            llm_predictor=llm_predictor, chunk_size_limit=512)

        index = GPTSimpleVectorIndex.from_documents(
            documents, service_context=service_context)
        response = index.query(
            "What did the author do growing up?",
            service_context=service_context,
            similarity_top_k=3
        )
        print(response)
        results.append(response)
