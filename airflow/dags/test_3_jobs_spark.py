import airflow
from airflow import DAG
from airflow.decorators import dag, task
from airflow.operators.empty import EmptyOperator
from airflow import DAG, datasets
from airflow.operators.python import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime, timedelta




dag = DAG(
    dag_id = "sparking_flow",
    default_args = {
        "owner": "hiep",
        "start_date": airflow.utils.dates.days_ago(1),
        "retries": 1,
        "retry_delay": timedelta(minutes=1)
    },
    schedule_interval = "@daily"
)

start = PythonOperator(
    task_id="start",
    python_callable = lambda: print("Jobs started"),
    dag=dag
)

python_job = SparkSubmitOperator(
    task_id="python_job",
    conn_id="spark_conn",
    application="/opt/airflow/dags/app/python/wordcountjob.py",
    verbose=1,
    name="PythonWordCount",
    dag=dag
)

scala_job = SparkSubmitOperator(
    task_id="scala_job",
    conn_id="spark_conn",
    application="/opt/airflow/dags/app/scala/target/scala-2.12/word-count_2.12-0.1.jar",
    verbose=1,
    dag=dag
)

java_job = SparkSubmitOperator(
    task_id="java_job",
    conn_id="spark_conn",
    application="/opt/airflow/dags/app/java/spark-job/target/spark-job-1.0-SNAPSHOT.jar",
    java_class="com.airscholar.spark.WordCountJob",
    verbose=1,
    dag=dag
)


end = PythonOperator(
    task_id="end",
    python_callable = lambda: print("Jobs completed successfully"),
    dag=dag
)

start >> [python_job, scala_job, java_job] >> end
