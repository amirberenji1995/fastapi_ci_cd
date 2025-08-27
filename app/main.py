from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"ok": True, "msg": "FastAPI CI/CD template is working!"}
