import sys 

from airflow import DAG
from  airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta

sys.path.append("/opt/airflow/python_scripts")

from insert_coinmarketcap_raw_data import insert_to_table_raw_coinmarketcap_api_data

default_args = {
    'description': "A DAG to orchestrate data", 
    'start_date': datetime(2026, 3, 6), 
    'catchup': False 
}
    
dag = DAG(
    dag_id='dags-orchestrator', 
    default_args=default_args, 
    schedule=timedelta(minutes=10)
)

with dag: 
    task1 = PythonOperator(
        task_id='test_task', 
        python_callable=insert_to_table_raw_coinmarketcap_api_data
    )
