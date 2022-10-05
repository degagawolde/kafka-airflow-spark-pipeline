from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd
import boto3

def s3Bucket(**context):
    print("insert_to_s3")
    data = context.get("ti").xcom_pull(key="data")
    print("data is {}".format(data))
    s3 = boto3.client("s3")


    bucket = ""
    # format name with current timestamp
    json_file_name = "json_file_" + datetime.now().strftime("%Y%m%d-%H%M%S") + ".json"
    s3object = s3.Object(bucket, json_file_name)

    s3object.put(Body=(bytes(json.dumps(data).encode("UTF-8"))))
    print("Updated")

with DAG(
    dag_id="dag",
    schedule_interval="@daily",
    default_args={
        "owner": "g5",
        "retries": 3,
        "retry_delay": timedelta(minutes=5),
        "start_date": datetime(2021, 1, 1),
    },
    
    catchup=False,
) as dags:

    s3Update = PythonOperator(
        task_id="update_s3",
        python_callable=s3Bucket,
        provide_context=True,
    )

s3Update