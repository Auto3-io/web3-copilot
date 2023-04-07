import promptlayer
import os
import sys

try:
    promptlayer.api_key = os.environ['PROMPTLAYER_API_KEY']
except KeyError:
    print('[error]: `PROMPTLAYER_API_KEY` environment variable required')
    sys.exit(1)


try:
    openai = promptlayer.openai
    openai.api_key = os.environ['OPENAI_API_KEY']
except KeyError:
    print('[error]: `OPENAI_API_KEY` environment variable required')
    sys.exit(1)
