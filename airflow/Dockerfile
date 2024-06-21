FROM apache/airflow:2.8.3-python3.10

USER root

RUN apt-get update && \
    apt-get install -y gcc python3-dev openjdk-17-jre-headless && \
    apt-get clean


# Set up environment variable
ENV JAVA_HOME /usr/lib/jvm/java-17-openjdk-amd64
ENV AIRFLOW__DATABASE__SQL_ALCHEMY_CONN postgresql+psycopg2://airflow:airflow@postgres:5432/airflow
ENV AIRFLOW_WEBSERVER_SECRET_KEY this_is_a_very_secured_key
ENV AIRFLOW__CORE__TEST_CONNECTION Enabled
ENV AIRFLOW__CORE__EXECUTOR LocalExecutor

USER airflow

COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r /requirements.txt