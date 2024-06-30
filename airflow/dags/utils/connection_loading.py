import json
from airflow import settings
from airflow.models import Connection

with open('/opt/airflow/dags/utils/connections.json', 'r') as f:
    conns_list = json.load(f)

session = settings.Session()
for conn_dict in conns_list:
    conn = Connection(
        conn_id=conn_dict['conn_id'],
        conn_type=conn_dict['conn_type'],
        host=conn_dict['host'],
        schema=conn_dict['schema'],
        login=conn_dict['login'],
        password=conn_dict['password'],
        port=conn_dict['port'],
        extra=conn_dict['extra']
    )
    session.add(conn)

session.commit()
