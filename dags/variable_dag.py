from datetime import datetime,timedelta
from airflow.models import DAG,Variable
from airflow.operators.python import PythonOperator

def print_variable():
    var_user_email=Variable.get("user_email")
    var_sample_json=Variable.get("sample_json",deserialize_json=True)

    return f"""
        var_user_email={var_user_email},
        var_sample_json={var_sample_json},
    """

default_args={
    'owner':'Raja',
    'retries':5,
    'retry_delay':timedelta(minutes=5)
}

with DAG(
    dag_id='Var_dag_07',
    default_args=default_args,
    start_date=datetime(2023,6,10),
    schedule_interval='@daily',
    catchup=False
) as dag:
    download_var=PythonOperator(
        task_id='dag_var',
        python_callable=print_variable
    )
    download_var