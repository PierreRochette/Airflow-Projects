import psycopg2

def connect_db(host, port, database, user, password): 
    
    conn = psycopg2.connect(
        host=host,
        port=port, 
        database=database, 
        user=user, 
        password=password
    )
    
    return conn, conn.cursor()
