from kafka import KafkaProducer
import json
from data import get_registed_user
import time


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


def get_partition(key, all, available):
    return 0


producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'],
                         value_serializer=json_serializer,
                         # partitioner=get_partition
                         )

if __name__ == "__main__":
    while 1 == 1:
        registered_user = get_registed_user()
        print(registered_user)
        producer.send("Topic1", registered_user)
        time.sleep(4)
        print("*************************")