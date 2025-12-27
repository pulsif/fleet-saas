from fastapi import FastAPI

app = FastAPI(title="Fleet SaaS API")

@app.get("/health")
def health():
    return {"status": "ok"}
