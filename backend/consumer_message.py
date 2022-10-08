import sys
sys.path.append("../scripts")
from kafka_utils import KafkaUtils


consumer = KafkaUtils.create_consumer(topic="g5-text-audio-pair")
print(consumer)
for msg in consumer:
    print(msg)
    print(msg.value)
    # break