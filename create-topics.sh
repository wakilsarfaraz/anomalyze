#!/bin/bash
echo "Creating kafka topics..."
kafka-topics --bootstrap-server kafka:9092 --create --topic anomalyze-topic --partitions 1 --replication-factor 1
echo "✅ Kafka topics created successfully."