from fetch_coinmarketcap_api import fetch_data
from connect_to_db import connect_db
from dotenv import load_dotenv
import os 
load_dotenv()

host=os.getenv("APP_POSTGRES_HOST")
port=os.getenv("APP_POSTGRES_PORT")
database=os.getenv("APP_POSTGRES_DB_COINMARKETCAP")
user=os.getenv("APP_POSTGRES_USER")
password=os.getenv("APP_POSTGRES_PASSWORD")

conn, cur = connect_db(host, port, database, user, password)

insert_query = """
INSERT INTO raw_coinmarketcap_api_data (
    coinmarketcap_id, name, symbol, 
    is_active, infinite_supply, is_fiat, 
    circulating_supply, total_supply, max_supply, 
    cmc_rank, price_symbol, price, 
    volume_24h, volume_change_24h, cex_volume_24h, 
    dex_volume_24h, percent_change_1h, percent_change_24h, 
    percent_change_7d, percent_change_30d, percent_change_60d, 
    percent_change_90d, market_cap, market_cap_dominance, 
    fully_diluted_market_cap
) VALUES (%s, %s, %s, %s, %s,
%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,
%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)
"""


data_to_insert=[]
data = fetch_data()
raw_data_list = data["data"]

for i in range(len(raw_data_list)): 
    
    data_list = raw_data_list[i]
    
    append_tuple = (
        data_list["id"], 
        data_list["name"], 
        data_list["symbol"], 
        True if data_list["is_active"] == 1 else False, # Convert int to bool
        data_list["infinite_supply"], 
        False if data_list["is_fiat"] == 0 else True, 
        data_list["circulating_supply"], 
        data_list["total_supply"], 
        data_list["max_supply"], 
        data_list["cmc_rank"], 
        data_list["quote"][0]["symbol"], 
        data_list["quote"][0]["price"], 
        data_list["quote"][0]["volume_24h"], 
        data_list["quote"][0]["volume_change_24h"],
        data_list["quote"][0]["cex_volume_24h"],
        data_list["quote"][0]["dex_volume_24h"],
        data_list["quote"][0]["percent_change_1h"],
        data_list["quote"][0]["percent_change_24h"],
        data_list["quote"][0]["percent_change_7d"],
        data_list["quote"][0]["percent_change_30d"],
        data_list["quote"][0]["percent_change_60d"],
        data_list["quote"][0]["percent_change_90d"],
        data_list["quote"][0]["market_cap"], 
        data_list["quote"][0]["market_cap_dominance"],
        data_list["quote"][0]["fully_diluted_market_cap"]
    )
    
    data_to_insert.append(append_tuple)
    
cur.executemany(insert_query, data_to_insert)
conn.commit()
print("Data successfully added to DB")
