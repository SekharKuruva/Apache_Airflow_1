from datetime import datetime,timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args={
    'owner':'Raja',
    'retries':5,
    'retry_delay':timedelta(minutes=5)  
}

def first():
    print("Hai this first python_operator dag")

def greet(ti):
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    age = ti.xcom_pull(task_ids='get_age', key='age')
    print(f"Hello World! My name is {first_name} {last_name}, "
          f"and I am {age} years old!")

def get_name(ti):
    ti.xcom_push(key='first_name', value='Raja')
    ti.xcom_push(key='last_name', value='sekhar')

def get_age(ti):
    ti.xcom_push(key='age', value=19)

with DAG(
    dag_id='dag_pythonoperator_18',
    default_args=default_args,
    description='This is the python operator dag',
    start_date=datetime(2023,6,2),
    schedule_interval='@daily'
) as dag:
    task1=PythonOperator(
        task_id='first_task',
        python_callable=first
    )
    task2 = PythonOperator(
        task_id='greet',
        python_callable=greet
    )
    task3 = PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )

    task4= PythonOperator(
        task_id='get_age',
        python_callable=get_age
    )
    task1 >> task3 >> task4 >> task2