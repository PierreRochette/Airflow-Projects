import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

try: 
    
    conn = psycopg2.connect(
        host=os.getenv("APP_POSTGRES_HOST"),
        database=os.getenv("APP_POSTGRES_DB_COINMARKETCAP"), 
        user=os.getenv("APP_POSTGRES_USER"), 
        password=os.getenv("APP_POSTGRES_PASSWORD"),
        port=os.getenv("APP_POSTGRES_PORT")
    )
    
    print("Successfully connected to database.")
    print("Creating table...")
    
    cur = conn.cursor()
    
    create_table_query = """
    CREATE TABLE IF NOT EXISTS raw_coinmarketcap_api_data (
        id SERIAL PRIMARY KEY, 
        coinmarketcap_id INTEGER, 
        name TEXT,
        symbol VARCHAR(10),
        is_active BOOLEAN, 
        infinite_supply BOOLEAN, 
        is_fiat BOOLEAN, 
        circulating_supply DOUBLE PRECISION,
        total_supply DOUBLE PRECISION, 
        max_supply DOUBLE PRECISION, 
        cmc_rank INTEGER, 
        price_symbol VARCHAR(10), 
        price DOUBLE PRECISION,
        volume_24h DOUBLE PRECISION,
        volume_change_24h DOUBLE PRECISION, 
        cex_volume_24h DOUBLE PRECISION, 
        dex_volume_24h DOUBLE PRECISION, 
        percent_change_1h DOUBLE PRECISION, 
        percent_change_24h DOUBLE PRECISION, 
        percent_change_7d DOUBLE PRECISION, 
        percent_change_30d DOUBLE PRECISION, 
        percent_change_60d DOUBLE PRECISION, 
        percent_change_90d DOUBLE PRECISION, 
        market_cap DOUBLE PRECISION, 
        market_cap_dominance DOUBLE PRECISION, 
        fully_diluted_market_cap DOUBLE PRECISION
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP;
    )
    """
    
    cur.execute(create_table_query)
    conn.commit()
    print("Table créée avec succès")
    cur.close()
    conn.close()
    
except Exception as e: 
    print("Error : ", e)