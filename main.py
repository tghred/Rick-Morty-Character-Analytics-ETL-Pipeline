import RequestsFunctions as RF
from PyEngPract.RequestsFunctions import save_csv

BASE_URL = 'https://rickandmortyapi.com/api/'
ENDPOINT = 'character'

data = RF.main_request(BASE_URL, ENDPOINT,page= 1)
print(data)
pages= RF.get_total_pages(data)
print(pages)
characters = RF.parse_caharacter_data(data)
print(characters)

all_characters = RF.get_all_characters(data)
print(all_characters)
df = RF.save_csv(all_characters)
