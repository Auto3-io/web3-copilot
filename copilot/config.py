import promptlayer
import os
import sys

try:
    promptlayer.api_key = os.environ['PROMPT_API_KEY']
    promptlayer.api_key = os.environ['PROMPT_API_KEY']
except KeyError:
    print('[error]: `PROMPT_API_KEY` environment variable required')
    sys.exit(1)


try:
    promptlayer.api_key = os.environ['OPENAI_API_KEY']
    openai = promptlayer.openai
    openai.api_key = os.environ['OPENAI_API_KEY']
except KeyError:
    print('[error]: `OPENAI_API_KEY` environment variable required')
    sys.exit(1)
