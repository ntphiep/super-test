import airflow
from airflow import DAG
from airflow.decorators import dag, task
# from airflow.operators.empty import EmptyOperator
# from airflow import DAG, datasets
# from airflow.operators.python import PythonOperator
# from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.sensors.filesystem import FileSensor
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.models.baseoperator import chain

from datetime import datetime, timedelta

now = datetime.now()

# @dag(
#     default_args={
#         "owner": "airflow",
#         "depends_on_past": False,
#         "email": ["ng.hiep0822@gmail.com"],
#         "start_date": datetime(now.year, now.month, now.day),
#         "email_on_failure": True,
#         "email_on_retry": True,
#         "retries": 1,
#         "retry_delay": timedelta(seconds=10),
#     },
#     schedule=timedelta(days=1),
#     tags=["super", "test"],
# )
# def test_gcp_tasks():
#     start = EmptyOperator(
#         task_id="start", 
#         dag=dag
#     )
        
#     # bash_task = BashOperator(
#     #     task_id="bash_task",
#     #     bash_command="echo 'Hello World'",
#     #     dag=dag
#     # )
        
#     chain(
#         start,
#         #bash_task
#     )
    
    
# test_gcp_tasks()



with DAG(
    dag_id="super_test_dag", 
    description="This DAG runs a simple Pyspark app.",
    default_args={
        "owner": "ntphiep",
        "depends_on_past": False,
        "start_date": datetime(now.year, now.month, now.day),
        "email": ["ng.hiep0822@gmail.com"],
        "email_on_failure": True,
        "email_on_retry":  False,
        "retries": 1,
        "retry_delay": timedelta(seconds=10),
    },
    schedule_interval=timedelta(days=1),
) as dag:
    start = EmptyOperator(
        task_id="start", 
        dag=dag
    )
        
    bash_task = BashOperator(
        task_id="bash_task",
        bash_command="echo 'Hello World'",
        dag=dag
    )
        
    chain(
        start,
        bash_task
    )