
from typing import List, Dict, Any
import  json
import csv

def save_to_json(characters:List[Dict], filename:str='characters.json'):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(characters, f, ensure_ascii=False, indent=2)
        print(F"Saved {filename}")
    except Exception as e:
        print(f"Failed to save {filename}: {e}")


def save_to_csv(characters:List[Dict],filename:str = 'char.csv'):
    if not characters:
        return

    filenames = characters[0].keys()

    with open(filename, 'w', newline='',encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=filenames)
        writer.writeheader()
        writer.writerows(characters)