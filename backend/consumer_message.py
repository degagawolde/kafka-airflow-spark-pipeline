import sys
sys.path.append("../scripts")
from all_kafka import AllKafka


consumer = AllKafka.create_consumer(topic="text.audio.pair")
print(consumer)
for msg in consumer:
    print(msg)
    print(msg.value)
    # break

