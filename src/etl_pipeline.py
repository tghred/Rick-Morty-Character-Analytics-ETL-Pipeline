import requests
from typing import List, Dict, Any
import  time
from .database.connection import db_connection
from .utils import parse_characters_data
from .utils.file_exporter import  save_to_csv,save_to_json

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




###################################################################

def save_to_postgres(all_characters:List[Dict[str, Any]]) -> bool:

    try:
        with db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "CREATE TABLE IF NOT EXISTS characters ( id INTEGER PRIMARY KEY, name VARCHAR(255) NOT NULL, status VARCHAR(50), species VARCHAR(100), episode_count INEGER, location VARCHAR(255));"
                    ""

                )
                for char in all_characters:
                    cursor.execute(
                        "INSERT INTO characters (id,name,status,species,episode_count,location) VALUES (?,?,?,?,?,?) ON CONFLICT (id) DO UPDATE SET name=EXCLUDE.name,status= EXCLUDE.status,species=EXCLUDE.species, ep_count=EXCLUDE.episode_count,location=EXCLUDE.location",

                    ),(
                        char.get('id'),
                        char.get('name','Unknown'),
                        char.get('status','Unknown'),
                        char.get('species','Unknown'),
                        char.get('episode_count','Unknown'),
                        char.get('location','Unknown'),
                    )
                conn.commit()
                print(f"Saved to postgres successfully")
                return True



    except Exception as e:
        print(e)
        return False



def main_etl_pipeline():
    print("Main ETL function executed")
    characters = get_all_characters()
    if not characters:
        print("Failed to get all characters")

    print("extract all characters")

    save_to_postgres(characters)

    save_to_json(characters, 'characters.json')
    save_to_csv(characters, 'characters.csv')
    print("Saved to postgres successfully")


