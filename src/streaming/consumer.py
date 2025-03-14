from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'anomalyze-topic',
    bootstrap_servers='kafka:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("✅ Kafka Consumer Started. Waiting for messages...")

for message in consumer:
    print(f"📩 Received: {message.value}")
