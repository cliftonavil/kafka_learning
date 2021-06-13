from kafka import KafkaConsumer
import json

if __name__ == '__main__':
    consumer = KafkaConsumer('Topic1',
                             bootstrap_servers=['127.0.0.1:9092'],
                             auto_offset_reset='earliest',
                             group_id='topic-group-a') # Any group id
    print('Started Consuming .......')
    for msg in consumer:
        print("Recived Data : ",json.loads(msg.value))