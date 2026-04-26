from fastapi import FastAPI
import redis
import uuid
import os
import time

app = FastAPI()

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))


# 👉 safer Redis connection (waits until Redis is ready)
def get_redis():
    for i in range(10):
        try:
            r = redis.Redis(
                host=REDIS_HOST,
                port=REDIS_PORT,
                decode_responses=True
            )
            r.ping()
            return r
        except Exception:
            print(f"Redis not ready... retry {i+1}/10")
            time.sleep(2)

    raise Exception("Could not connect to Redis")


r = get_redis()


@app.get("/")
def root():
    return {"message": "API is running"}


@app.get("/health")
def health():
    try:
        r.ping()
        return {"message": "healthy"}
    except Exception:
        return {"message": "unhealthy"}


@app.post("/jobs")
def create_job():
    job_id = str(uuid.uuid4())
    r.lpush("job", job_id)
    r.hset(f"job:{job_id}", "status", "queued")
    return {"job_id": job_id}


@app.get("/jobs/{job_id}")
def get_job(job_id: str):
    status = r.hget(f"job:{job_id}", "status")

    if not status:
        return {"error": "not found"}

    return {
        "job_id": job_id,
        "status": status
    }
