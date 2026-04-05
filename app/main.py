from fastapi import FastAPI

app = FastAPI(title="FastAPI CI/CD Demo")

@app.get("/")
def root():
    return {"message": "Hello from FastAPI CI/CD Demo! 🚀"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/info")
def info():
    return {
        "app": "fastapi-cicd-demo",
        "version": "1.0.0",
        "author": "Mohammed Anas"
    }
