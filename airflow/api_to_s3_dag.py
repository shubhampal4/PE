from airflow import DAG
from airflow.decorators import task
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from airflow.utils.task_group import TaskGroup
from airflow.utils.trigger_rule import TriggerRule
import time
import requests
import boto3

default_args = {
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

with DAG("api_to_s3_pipeline", default_args=default_args, start_date=days_ago(1), schedule_interval="@daily") as dag:

    @task
    def extract_data():
        response = requests.get("https://api.example.com/data")
        return response.json()

    @task
    def transform_data(data):
        return {"processed": data[:10]}

    @task
    def load_to_s3(data):
        s3 = boto3.client("s3")
        s3.put_object(Bucket="my-bucket", Key="data.json", Body=str(data))

    data = extract_data()
    transformed = transform_data(data)
    load_to_s3(transformed)
