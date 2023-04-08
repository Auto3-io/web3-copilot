from pathlib import Path
import yaml

from copilot.method_search_engine.engine import search_engine

import nest_asyncio
nest_asyncio.apply()

p = Path(__file__).with_name('steps_input.yaml')
with p.open('r') as f:
    steps = yaml.safe_load(f.read())['steps']

outputs = search_engine([step['action'] for step in steps])

print(outputs)
