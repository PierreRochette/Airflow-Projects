import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

try: 
    
    conn = psycopg2.connect(
        host=os.getenv("APP_POSTGRES_HOST"),
        database=os.getenv("APP_POSTGRES_DB"), 
        user=os.getenv("APP_POSTGRES_USER"), 
        password=os.getenv("APP_POSTGRES_PASSWORD"),
        port=os.getenv("APP_POSTGRES_PORT")
    )
    
    print("Successfully connected to database.")
    print("Creating table...")
    
    cur = conn.cursor()
    
    create_table_query = """
    CREATE TABLE IF NOT EXISTS raw_api_data (
        id SERIAL PRIMARY KEY, 
        coinmarketcap_id INTEGER, 
        name TEXT,
        symbol VARCHAR(10),
        is_active BOOLEAN, 
        infinite_supply BOOLEAN, 
        is_fiat BOOLEAN, 
        circulating_supply NUMERIC(20,8),
        total_supply NUMERIC(20,8), 
        max_supply NUMERIC(20,8), 
        cmc_rank INTEGER, 
        quote_symbol VARCHAR(10), 
        price NUMERIC(20,8),
        volume_24h NUMERIC(20,8),
        volume_change_24h NUMERIC(20,8), 
        cex_volume_24h NUMERIC(20,8), 
        dex_volume_24h NUMERIC(20,8), 
        percent_change_1h NUMERIC(20,8), 
        percent_change_24h NUMERIC(20,8), 
        percent_change_7d NUMERIC(20,8), 
        percent_change_30d NUMERIC(20,8), 
        percent_change_60d NUMERIC(20,8), 
        percent_change_90d NUMERIC(20,8), 
        market_cap NUMERIC(20,8), 
        marker_cap_dominance NUMERIC(20,8), 
        fully_diluted_market_cap NUMERIC(20,8)          
    )
    """
    
    cur.execute(create_table_query)
    conn.commit()
    print("Table créée avec succès")
    cur.close()
    conn.close()
    
except Exception as e: 
    print("Error : ", e)