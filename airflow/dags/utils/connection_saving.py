import json
from airflow import settings
from airflow.models import Connection

session = settings.Session()
conns = session.query(Connection).all()

conns_list = []
for conn in conns:
    conns_list.append({
        "conn_id": conn.conn_id,
        "conn_type": conn.conn_type,
        "host": conn.host,
        "schema": conn.schema,
        "login": conn.login,
        "password": conn.password,
        "port": conn.port,
        "extra": conn.extra
    })

with open('/opt/airflow/dags/utils/connections.json', 'w') as f:
    json.dump(conns_list, f)
