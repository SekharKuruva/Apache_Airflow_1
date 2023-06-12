from datetime import datetime,timedelta

from airflow.decorators import dag,task

default_args={
    'owner':'Raja',
    'retries':5,
    'retry_delay':timedelta(minutes=5)
}

@dag(dag_id='dag_api',
     default_args=default_args,
     start_date=datetime(2023,6,10),
     schedule_interval='@daily')
def hellow_world():
    @task()
    def get_name():
        return 'Raja'
    
    @task()
    def get_age():
        return 20
    
    @task()
    def greet(name,age):
        print(f'hellow world!!! my name is {name} and age is {age}')
    
    name=get_name()
    age=get_age()
    greet(name=name,age=age)
greet_dag=hellow_world()