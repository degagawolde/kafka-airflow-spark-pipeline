import sys
sys.path.append("../scripts")
from kafka_utils import KafkaUtils
import pandas as pd


df = pd.read_csv("../data/amharic_news_dataset.csv")
producer = KafkaUtils.create_producer()

for row in df.itertuples():
    producer.send("g5-untranscribed-text", value=row.article)
    print(type(row.article))
    print(row.article)
    # break