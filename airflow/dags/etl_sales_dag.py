from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
import os, csv, psycopg2

DEFAULT_ARGS = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}

def load_csv_to_postgres(**kwargs):
    pg_host = os.getenv('POSTGRES_HOST', 'postgres')
    conn = psycopg2.connect(host=pg_host, dbname='ecommerce', user='postgres', password='postgres')
    cur = conn.cursor()
    cur.execute("CREATE SCHEMA IF NOT EXISTS raw;")
    cur.execute("""
    CREATE TABLE IF NOT EXISTS raw.sales (
        order_id TEXT,
        order_date DATE,
        customer_id TEXT,
        product_id TEXT,
        quantity INTEGER,
        price NUMERIC
    );
    """)
    conn.commit()
    data_path = '/opt/airflow/data/orders.csv'
    rows = []
    with open(data_path, 'r') as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append((r['order_id'], r['order_date'], r['customer_id'], r['product_id'], int(r['quantity']), float(r['price'])))
    cur.execute('TRUNCATE raw.sales;')
    if rows:
        cur.executemany('INSERT INTO raw.sales(order_id, order_date, customer_id, product_id, quantity, price) VALUES (%s,%s,%s,%s,%s,%s);', rows)
    conn.commit()
    cur.close()
    conn.close()
    print(f'Loaded {len(rows)} rows into raw.sales')

with DAG(
    dag_id='etl_sales_dag',
    default_args=DEFAULT_ARGS,
    schedule_interval=None,
    start_date=datetime(2023,1,1),
    catchup=False,
    tags=['etl','portfolio'],
) as dag:

    task_load_csv = PythonOperator(
        task_id='load_csv_to_postgres',
        python_callable=load_csv_to_postgres,
    )

    task_run_dbt = BashOperator(
        task_id='run_dbt',
        bash_command='cd /opt/airflow/dbt && ~/.local/bin/dbt deps && ~/.local/bin/dbt seed --profiles-dir . && ~/.local/bin/dbt run --profiles-dir . && ~/.local/bin/dbt test --profiles-dir .',
    )

    task_load_csv >> task_run_dbt
