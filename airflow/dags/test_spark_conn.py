from airflow import DAG
from airflow.decorators import dag, task
from airflow.operators.empty import EmptyOperator
# from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
# import os
from utils.slack_alert import task_fail_slack_alert

###############################################
# Parameters
###############################################


# spark_master = "spark://spark-master:7077"
spark_app_name = "CLM"
# file_path = "./app/hello_world.py"

now = datetime.now()

default_args = {
    "owner": "ntphiep",
    "depends_on_past": False,
    "start_date": datetime(now.year, now.month, now.day),
    "email": ["ng.hiep0822@gmail.com"],
    "email_on_failure": True,
    "email_on_retry":  False,
    "retries": 1,
    "retry_delay": timedelta(seconds=10),
    "on_failure_callback": task_fail_slack_alert,
}

dag = DAG(
        dag_id="spark-test", 
        description="This DAG runs a simple Pyspark app.",
        default_args=default_args, 
        schedule=timedelta(days=1),
    )

start = EmptyOperator(
    task_id="start", 
    dag=dag
)

date_bash_job = BashOperator(
    task_id="date_bash_job",
    bash_command="date > /opt/airflow/dags/utils/date.txt",
    dag=dag
)

spark_job = SparkSubmitOperator(
    task_id="spark_job",
    application="/opt/airflow/dags/app/python/wordcountjob.py", # Spark application path created in airflow and spark cluster
    name=spark_app_name,
    conn_id="spark_conn",
    verbose=1,
    dag=dag
)

end = EmptyOperator(
    task_id="end", 
    dag=dag,
    trigger_rule="all_done"
)

start >> [date_bash_job, spark_job] >> end   

