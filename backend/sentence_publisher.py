import sys
sys.path.append("../scripts")
from all_kafka import AllKafka
import pandas as pd


df = pd.read_csv("../data/transcription_text.csv")
producer = AllKafka.create_producer()

for row in df.itertuples():
    producer.send("text", value=row.text)
    print(type(row.text))
    print(row.text)
    # break
