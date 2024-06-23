from airflow import DAG, models
from airflow.decorators import dag, task
from datetime import datetime, timedelta
# from airflow.contrib.operators.dataflow_operator import DataFlowPythonOperator
from airflow.contrib.sensors.gcs_sensor import GoogleCloudStoragePrefixSensor
from airflow.contrib.hooks.gcs_hook import GoogleCloudStorageHook
# from airflow.operators.python_operator import PythonOperator

from airflow.providers.google.cloud.hooks.gcs import GCSHook
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
# from airflow.providers.google.cloud.sensors.gcs import GCSFileSensor

now = datetime.now()

@dag(
    default_args={
        "owner": "airflow",
        "depends_on_past": False,
        "email": ["ng.hiep0822@gmail.com"],
        "start_date": datetime(now.year, now.month, now.day),
        "email_on_failure": True,
        "email_on_retry": True,
        "retries": 1,
        "retry_delay": timedelta(seconds=10),
    },
    schedule=timedelta(days=1),
    tags=["gcp", "test"],
)
def test_gcp_tasks():
    @task()
    def start():
        print("Start")
        
    
    @task()
    def list_gcs_files(bucket_name: str, prefix: str):
        hook = GCSHook()
        files = hook.list(bucket_name, prefix=prefix)
        print(files)

    # @task()
    # def list_gcs_files_with_sensor(bucket_name: str, prefix: str):
    #     hook = GCSHook()
    #     files = hook.list(bucket_name, prefix=prefix)
    #     print(files)

    # list_gcs_files("airflow-dags", "app/python")
    # list_gcs_files_with_sensor("airflow-dags", "app/python")
    
    start() >> list_gcs_files("airflow-dags", "app/python")
    

dag = test_gcp_tasks()