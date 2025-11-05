import requests
from typing import List, Dict, Any
import  time
import csv

BASE_URL = 'https://rickandmortyapi.com/api/'
ENDPOINT = 'character'

###################______________________________##############################

def main_request(base_url:str,endpoint:str,page:int)->Dict[str, Any]:
    """
    Main Request Function
    :param base_url:
    :param endpoint:
    :param page:
    :return: DICTIONARY OF JSON FILE
    """
    try:
        url = f"{base_url}{endpoint}?page={page}"

        headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'Accept': 'application/json',
        }

        response = requests.get(url,headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()


    except requests.exceptions.HTTPError as e:

        print(f"HTTP Error at page {page}: {e}")

        if response.status_code == 404:
            print(f"Page {page} not found - likely end of data")

        return None

    except requests.exceptions.ConnectionError as e:
        print(f"Connection Error at page {page}: {e}")
        return None

    except requests.exceptions.Timeout as e:
        print(f"Timeout Error at page {page}: {e}")
        return None

    except requests.exceptions.RequestException as e:
        print(f"Request Exception at page {page}: {e}")
        return None

    except ValueError as e:
        print(f"JSON Decode Error at page {page}: {e}")
        return None



############################_______________________________#########################

def get_total_pages(response:Dict[str,Any])->int:
    """
    Extraxt total number of pages
    :param response: as a dectionary variable
    :return: integer variable total number of pages
    """
    return response.get('info',{}).get('pages',0)

#######################________________________________##############################

def parse_caharacter_data(response:Dict[str,Any])->List[Dict[str, Any]]:
    """
     Get characters data in spesific page like (id,name,location, no of episodes...etc)
    :param response: dictionary
    :return: a list of dictionary
    """
    character_list = []
    if not response or 'results' not in response:
        return character_list

    for character in response['results']:
        character_data = {
            'id': character.get('id'),
            'name': character.get('name','Unknown'),
            'sataus': character.get('sataus','Unknown'),
            'species' : character.get('species','Unknown'),
            'episode_count' : len(character.get('episodes',[])),
            'location': character.get('location','Unknown').get('name','Unknown')
        }
        character_list.append(character_data)

    return character_list

###################_______________________#############################

def get_all_characters(response:Dict[str,Any])-> List[Dict[str, Any]]:
    """
    Get all characters data from all pages
    :param response:
    :return: list of dictionaries
    """
    all_characters = []
    frist_page_data = main_request(BASE_URL,ENDPOINT,1)

    if not frist_page_data or 'results' not in frist_page_data:
        return all_characters

    total_pages = get_total_pages(frist_page_data)
    print(f"{total_pages} total pages")

    for page in range(1,total_pages+1):
        print(f"Getting page {page} from {total_pages}..")

        page_data = main_request(BASE_URL,ENDPOINT,page)
        characters = parse_caharacter_data(page_data)
        all_characters.extend(characters)
        time.sleep(0.1)

    return all_characters



####################################################################

def save_csv(characters:List[Dict],filename:str = 'char.csv'):
    if not characters:
        return

    filenames = characters[0].keys()

    with open(filename, 'w', newline='',encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=filenames)
        writer.writeheader()
        writer.writerows(characters)


def save_to_json(characters: List[Dict], filename: str = 'characters.json'):
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(characters, f, ensure_ascii=False, indent=2)

###################################################################

if __name__ == "__main__":
    # اختبار الدالة
    all_characters = get_all_characters(main_request(BASE_URL,ENDPOINT,1))
    print(f"Getting {len(all_characters)} characters")

    for character in all_characters[:5]:
        print(character)
