from confluent_kafka import Consumer
import json,uuid

consumer_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'order-tracker',
    'auto.offset.reset': 'earliest'
}
consumer = Consumer(consumer_config)

consumer.subscribe(['orders'])

print("Consumer started. Waiting for messages...")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue

        order = json.loads(msg.value().decode('utf-8'))
        print("Received order: {}".format(order))

except KeyboardInterrupt:
    print("Consumer interrupted. Closing...")
finally:
    consumer.close()