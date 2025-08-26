from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"ok": True, "msg": "Hello from FastAPI template"}
