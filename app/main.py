from fastapi import FastAPI, Response
from prometheus_client import (
    CONTENT_TYPE_LATEST,
    Counter,
    generate_latest,
)

app = FastAPI(title="DevSecOps Demo API")

REQUEST_COUNT = Counter(
    "app_request_total",
    "Total permintaan HTTP ke aplikasi",
    ["endpoint"],
)


@app.get("/health")
def health_Check():
    REQUEST_COUNT.labels(endpoint="/health").inc()
    return {"status": "ok"}


@app.get("/metrics")
def metrics():
    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST,
    )
