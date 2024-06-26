from airflow.hooks.base import BaseHook
from airflow.providers.slack.operators.slack_webhook import SlackWebhookOperator

SLACK_CONN_ID = 'slack'

# url = "https://hooks.slack.com/services/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"


def task_fail_slack_alert(context):
    slack_webhook_token = BaseHook.get_connection(SLACK_CONN_ID).password
    slack_msg = """
        Task Failed.
        *DAG*: {dag_id}
        *Task*: {task}
        *Dag*: {dag}
        *Execution Time*: {exec_date}
        *Log Url*: {log_url}
    """.format(
        dag_id=context.get('dag').dag_id,
        task=context.get('task_instance').task_id,
        dag=context.get('task_instance').dag_id,
        ti=context.get('task_instance'),
        exec_date=context.get('execution_date'),
        log_url=context.get('task_instance').log_url,
    )
    
    failed_alert = SlackWebhookOperator(
        task_id='slack_alert',
        slack_webhook_conn_id=SLACK_CONN_ID,
        message=slack_msg,
        username='airflow')
    
    return failed_alert.execute(context=context)