import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
products=json.loads((ROOT/'data/products.json').read_text(encoding='utf-8'))
for p in products:
    print(f"# {p['name']}\n\n## Perché valutarlo\n{p['description']}\n\n### Pro\n" + ''.join(f"- {x}\n" for x in p.get('pros',[])) + "\n### Contro\n" + ''.join(f"- {x}\n" for x in p.get('cons',[])))
