curl http://localhost:8000/

curl -X POST http://localhost:8000/api/ingest \
-H "Content-Type: application/json" \
-d '{"source": "production-db-test", "timestamp": "2025-03-08T12:00:00Z", "data": {"value": 111}}'


docker exec -it anomalyze-mongodb mongosh anomalyze --eval 'db.ingestion_data.find({source:"production-db-test"}).pretty()'


docker exec -it anomalyze-mongodb-test mongosh anomalyze_test --eval 'db.ingestion_data.insertOne({source:"test-db-check", timestamp:"2025-03-08T12:10:00Z", data: {value: 222}})'

docker exec -it anomalyze-mongodb-test mongosh anomalyze_test --eval 'db.ingestion_data.find({source:"test-db-check"}).pretty()'

