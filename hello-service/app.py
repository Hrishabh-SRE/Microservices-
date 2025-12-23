from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Define a Metric: This counts how many times the hello endpoint is hit
REQUEST_COUNT = Counter('hello_service_requests_total', 'Total count of requests to the hello endpoint')

@app.route('/')
def index():
    return jsonify(message="Welcome to the hello-service!")

@app.route('/hello')
def hello():
    # Increment our metric every time this endpoint is called
    REQUEST_COUNT.inc()
    return jsonify(service="hello-service", status="active", greet="Hello, World!")

@app.route('/metrics')
def metrics():
    # This is the endpoint the scraper will hit
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    print("Starting hello-service on http://localhost:5000")
    print("Available endpoints:")
    print("  - http://localhost:5000/")
    print("  - http://localhost:5000/hello")
    print("  - http://localhost:5000/metrics")
    app.run(host='0.0.0.0', port=5000, debug=True)