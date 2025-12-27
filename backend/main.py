from fastapi import FastAPI

app = FastAPI(title="Fleet SaaS API")

@app.get("/")
def root():
    return {"message": "Fleet SaaS API running"}

@app.get("/health")
def health():
    return {"status": "ok"}
