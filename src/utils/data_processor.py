"""
Data Processing Functions
"""
from typing import List, Dict, Any


def parse_characters_data(response: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
   Character data analysis35
    """
    characters_list = []

    if not response or 'results' not in response:
        return characters_list

    for character in response['results']:
        character_data = {
            'id': character.get('id'),
            'name': character.get('name', 'Unknown'),
            'status': character.get('status', 'Unknown'),
            'species': character.get('species', 'Unknown'),
            'episode_count': len(character.get('episode', [])),
            'location': character.get('location', {}).get('name', 'Unknown')
        }
        characters_list.append(character_data)

    return characters_list


def clean_character_data(characters: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Cleaning and reprocessing characters data
    """
    cleaned_data = []

    for char in characters:
        cleaned_char = char.copy()
        if 'name' in cleaned_char:
            cleaned_char['name'] = cleaned_char['name'].strip()
        if 'species' in cleaned_char:
            cleaned_char['species'] = cleaned_char['species'].title()
        cleaned_data.append(cleaned_char)

    return cleaned_data
