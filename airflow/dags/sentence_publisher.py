from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd

from kafka import KafkaProducer

def sentence_publisher():
    df = pd.read_csv("/mnt/10ac-batch-6/notebooks/degaga_wolde/amharic_news_dataset.csv")
    producer = KafkaProducer(bootstrap_servers='b-1.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092',
                            value_serializer=lambda x: dumps(x).encode('utf-8'))
    for row in df.itertuples():
        producer.send("g5-untranscribed-text", value=row.article)
        print(type(row.article))
        print(row.article)

  
with DAG( 
    dag_id="dag",
    schedule_interval="@daily",
    default_args={
        "owner": "g5",
        "retries": 3,
        "retry_delay": timedelta(minutes=5),
        "start_date": datetime(2022, 1, 1),
    },
    
    catchup=False,
) as dags:

     text_publisher = PythonOperator(
        task_id="publish-sentence-to-kafka-topic",
        python_callable=sentence_publisher,
        provide_context=True,
     )

text_publisher
