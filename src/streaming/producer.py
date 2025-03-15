from kafka import KafkaProducer
import json
import time

try:
    print("✅ Starting Kafka Producer...")  # Debugging print

    producer = KafkaProducer(
        bootstrap_servers='kafka:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    print("✅ Kafka Producer Connected Successfully!")  # Debugging print

    for i in range(10):
        message = {"sensor_id": 1, "value": i, "status": "ok"}
        print(f"➡️ Sending message: {message}")  # Debugging print
        producer.send('anomalyze-topic', value=message)
        producer.flush()
        time.sleep(1)

    print("✅ All messages sent!")  # Debugging print

except Exception as e:
    print(f"❌ Error: {e}")
