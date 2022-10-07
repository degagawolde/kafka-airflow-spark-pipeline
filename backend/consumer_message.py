import sys
sys.path.append("../scripts")
from all_kafka import AllKafka


consumer = AllKafka.create_consumer(topic="g5-audio-text-pair")
print(consumer)
for msg in consumer:
    print(msg)
    print(msg.value)
    # break

