curl -X 'POST' 'http://localhost:8000/api/ingest' \
-H 'Content-Type: application/json' \
-d '{"source": "sensor-1", "timestamp": "2025-03-10T21:20:00Z", "data": {"temperature": 25.6}}'

