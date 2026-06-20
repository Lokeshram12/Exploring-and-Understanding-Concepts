from confluent_kafka import Producer
import json,uuid

producer_cofig = {
    'bootstrap.servers': 'localhost:9092',
}
producer = Producer(producer_cofig)

order = {
    "order_id": str(uuid.uuid4().hex),
    "user": "John Doe",
    "product": "Widget",
    "quantity": 3,
    "price": 19.99
}

def delivery_report(err, msg):
    if err is not None:
        print(f"Failed to deliver message: {err}")
    else:
        print(f"Message delivered to {msg.value()}")

producer.produce(
    topic='orders', 
    key=order['order_id'],
    value=json.dumps(order),
    callback=delivery_report)

producer.flush()