import promptlayer
import os
import sys
import openai as the_real_openai
from langchain.chat_models import PromptLayerChatOpenAI, ChatOpenAI as RealChatOpenAI

user_prompt_layer = False

openai = promptlayer.openai
ChatOpenAI = PromptLayerChatOpenAI

try:
    promptlayer.api_key = os.environ['PROMPTLAYER_API_KEY']
    print("promptlayer is enabled")
    user_prompt_layer = True
except KeyError:
    pass


try:
    if not user_prompt_layer:
        ChatOpenAI = RealChatOpenAI
        openai = the_real_openai
    openai.api_key = os.environ['OPENAI_API_KEY']
except KeyError:
    print('[error]: `OPENAI_API_KEY` environment variable required')
    sys.exit(1)

__all__ = ['openai', 'user_prompt_layer', 'ChatOpenAI']
