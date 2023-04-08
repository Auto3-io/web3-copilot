from llama_index import GPTTreeIndex, SimpleDirectoryReader, LLMPredictor, ServiceContext, PromptHelper, SummaryPrompt, GPTSimpleVectorIndex
from langchain.chat_models import PromptLayerChatOpenAI
from pathlib import Path

import nest_asyncio
# nest_asyncio.apply()

doc_dir = (Path(__file__) / '../../../docs').resolve()


documents = SimpleDirectoryReader(
    str(doc_dir), exclude=['*.sh'], recursive=True).load_data()

llm_predictor = LLMPredictor(llm=PromptLayerChatOpenAI(
    temperature=0, model_name="gpt-3.5-turbo", max_tokens=1024))


max_input_size = 3070
num_output = 1024
max_chunk_overlap = 4
prompt_helper = PromptHelper(max_input_size, num_output, max_chunk_overlap)
service_context = ServiceContext.from_defaults(
    llm_predictor=llm_predictor, prompt_helper=prompt_helper, chunk_size_limit=512)

SUMMARY_PROMPT = (
    "Write a summary of the following. Try to use only the "
    "information provided. Try to include as many key details as possible."
    "For method and its signature. You should keep signature with name and type at least."
    "And give a clear and precise guide of how to use it.\n"
    "\n"
    "\n"
    "{context_str}\n"
    "\n"
    "\n"
    'SUMMARY:"""\n'
)

# index = GPTTreeIndex.from_documents(
    # documents, summary_template=SummaryPrompt(SUMMARY_PROMPT),  service_context=service_context, num_children=3, use_async=True)
index = GPTSimpleVectorIndex.from_documents(documents, service_context=service_context)

index.save_to_disk('./index.json')
