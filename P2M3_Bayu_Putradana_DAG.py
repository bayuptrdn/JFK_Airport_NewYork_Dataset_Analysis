from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

import pandas as pd
import datetime as dt
import psycopg2 as db
from elasticsearch import Elasticsearch, helpers
from datetime import timedelta

# ======================
# Extract: Fetch data dari PostgreSQL
# ======================
def extract_data():
    conn_string = (
        "dbname='milestone_3' "
        "host='postgres' "
        "user='airflow' "
        "password='airflow' "
        "port='5432'"
    )
    conn = db.connect(conn_string)

    query = "SELECT * FROM table_m3;"
    df = pd.read_sql(query, conn)

    df.to_csv('/opt/airflow/dags/P2M3_Bayu_Putradana_data_raw.csv', index=False)
    print("Extract selesai: data disimpan ke P2M3_Bayu_Putradana_data_raw.csv")


# ======================
# Transform: Data Cleaning
# ======================
def transform_data():
    df = pd.read_csv('/opt/airflow/dags/P2M3_Bayu_Putradana_data_raw.csv')

    # Hapus data duplikat
    df = df.drop_duplicates()

    # Normalisasi nama kolom
    cleaned_columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(' ', '_')
        .str.replace('-', '_')
        .str.replace(r'[^a-z0-9_]', '', regex=True)
    )
    df.columns = cleaned_columns

    # Handling missing values
    for col in df.columns:
        if df[col].dtype in ['float64', 'int64']:
            df[col] = df[col].fillna(df[col].mean())
        else:
            if not df[col].mode().empty:
                df[col] = df[col].fillna(df[col].mode()[0])
            else:
                df[col] = df[col].fillna("unknown")

    # Simpan hasil cleaning
    df.to_csv('/opt/airflow/dags/P2M3_Bayu_Putradana_data_clean.csv', index=False)
    print("Transform selesai: data clean disimpan ke P2M3_Bayu_Putradana_data_clean.csv")


# ======================
# Load: Post to Elasticsearch
# ======================
def load_to_elasticsearch():
    es = Elasticsearch("http://elasticsearch:9200")

    df = pd.read_csv('/opt/airflow/dags/P2M3_Bayu_Putradana_data_clean.csv')



    actions = [                             # utk menambahkan index ke kibana dari elastic search
    {
        "_index": "flightjfk",
        "_id": i,
        "_source": r.to_dict()
    }
    for i,r in df.iterrows()
    ]

    response = helpers.bulk(es, actions)
    print(response)

# ======================
# Default Arguments & DAG Definition
# ======================
default_args = {
    'owner': 'bayu',
    'start_date': dt.datetime(2024, 11, 1, 9, 10),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

schedule = "10,20,30 9 * * 6"

with DAG(
    'postgres_etl_to_elasticsearch',
    default_args=default_args,
    schedule_interval=schedule,
    catchup=False,
    description='ETL otomatis PostgreSQL ke Elasticsearch'
) as dag:

    start_task = BashOperator(
        task_id='start_message',
        bash_command='echo "ETL dimulai..."'
    )

    extract_task = PythonOperator(
        task_id='fetch_from_postgresql',
        python_callable=extract_data
    )

    transform_task = PythonOperator(
        task_id='data_cleaning',
        python_callable=transform_data
    )

    load_task = PythonOperator(
        task_id='post_to_elasticsearch',
        python_callable=load_to_elasticsearch
    )

    end_task = BashOperator(
        task_id='end_message',
        bash_command='echo "ETL selesai!"'
    )

    start_task >> extract_task >> transform_task >> load_task >> end_task

