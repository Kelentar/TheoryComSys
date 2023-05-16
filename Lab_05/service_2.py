from kafka import KafkaConsumer

topic = 'common'

bootstrap_servers = ['kafka:9092']
group_id = 'my-group'

consumer = KafkaConsumer(topic, group_id=group_id, bootstrap_servers=bootstrap_servers)

for message in consumer:
    print(message.value.decode())
