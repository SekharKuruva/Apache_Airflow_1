from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from datetime import datetime,timedelta
import os

default_args = {
    'owner': 'Raja',
    'start_date': datetime(2023, 6, 9),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

def upload_to_s3():
    filename = '/opt/airflow/dags/main.txt'
    key = 'main.txt'
    bucket_name = 's3firstexample'

    hook = S3Hook('S3_conn')
    hook.load_file(filename=filename, key=key, bucket_name=bucket_name)
    print('File uploaded to S3.')

with DAG(
    dag_id='s3_upload_dag_20', 
    default_args=default_args, 
    schedule_interval=None,
    ) as dag:
    upload_task = PythonOperator(
        task_id='upload_to_s3',
        python_callable=upload_to_s3
    )
    upload_task