from datetime import datetime,timedelta
from airflow import DAG
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.operators.python_operator import PythonOperator
import boto3


default_args = {
    'owner': 'Raja',
    'start_date': datetime(2023, 6, 9),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

def start():
    print("Task is started!!")

def download_s3_file():
    s3_client = boto3.client('s3',region_name='us-east-2',
    aws_access_key_id='AKIASICZTMINOIDBYJDG',
    aws_secret_access_key='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'
)


    key = 'main.txt'
    bucket_name = 's3firstexample'
    local_filepath = '/opt/airflow/dags/main.txt'
    
    s3_client.download_file(bucket_name, key, local_filepath)

def end():
    print("Task is end!!!")

with DAG(
    dag_id='s3_download_dag_11',
    default_args=default_args,
    start_date=datetime(2023, 6, 12),
    schedule_interval=None,
    catchup=False
) as dag:
    task_1=PythonOperator(
        task_id='Start_task',
        python_callable=start
    )
    download_task = PythonOperator(
        task_id='download_s3_file_task',
        python_callable=download_s3_file
    )
    task_2=PythonOperator(
        task_id='end_task',
        python_callable=end
    )
    task_1 >> download_task >>task_2

