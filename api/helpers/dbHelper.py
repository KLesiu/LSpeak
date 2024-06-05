import json
from typing import Dict, List
# Wczytaj dane z pliku JSON
def load_data() -> Dict[str, List[Dict[str, str]]]:
    with open('db.json', 'r', encoding='utf-8') as f:
        return json.load(f)