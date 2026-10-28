from fastapi import FastAPI

app = FastAPI()


@app.get("/sante")
def sante():
    return {"ok": True}
