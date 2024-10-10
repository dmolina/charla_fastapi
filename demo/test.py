from fastapi import FastAPI  # , Path, Query

app = FastAPI()


@app.get("/")
def hello():
    return {"msg": "Hola a todo el  mundo"}
