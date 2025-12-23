# Hello Service

A simple Flask microservice with Prometheus metrics.

## Setup

1. Create and activate a virtual environment (if not already done):
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Service

### Option 1: Using the run script
```bash
./run.sh
```

### Option 2: Manual activation
```bash
source venv/bin/activate
python app.py
```

The service will start on `http://localhost:5000`

## Endpoints

- `GET /` - Welcome message
- `GET /hello` - Hello endpoint with service status
- `GET /metrics` - Prometheus metrics endpoint

## Testing

Once the service is running, you can test it with:

```bash
curl http://localhost:5000/
curl http://localhost:5000/hello
curl http://localhost:5000/metrics
```

