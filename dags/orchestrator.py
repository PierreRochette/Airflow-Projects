import sys 

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

sys.path.append("/opt/airflow/python_scripts")
from hello_world import main 



default_args = {
    'description':"A DAG to orchestrate data", 
    'start_date':datetime(2026, 2, 26), 
    'catchup':False 
}
    

dag = DAG(
    dag_id='test-orechestrator', 
    default_args=default_args, 
    schedule=timedelta(minutes=5)
)

with dag: 
    task1 = PythonOperator(
        task_id='test_task', 
        python_callable=main
    )
