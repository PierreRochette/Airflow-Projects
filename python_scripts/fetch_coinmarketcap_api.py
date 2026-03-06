from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from dotenv import load_dotenv
import os 

load_dotenv()
COINMARKETCAP_API_KEY = os.getenv('COINMARKETCAP_API_KEY')

url='https://pro-api.coinmarketcap.com/v3/cryptocurrency/quotes/latest'

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': COINMARKETCAP_API_KEY, 
}

parameters = {
    'id': '1,1027,3408'
}

session = Session()
session.headers.update(headers)

def fetch_data():
    
    try: 
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
    except (ConnectionError, Timeout, TooManyRedirects) as e: 
        print(f"The following error occured : {e}")
    finally: 
        return data