import time
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='kafka:9092')

while True:
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    producer.send('common', value=current_time.encode('utf-8'))
    time.sleep(5)