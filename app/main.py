from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/api")
def read_root():
    return {"Hello": "service1"}


@app.get("/api/go")
def read_item():
    return {'service2': 'success go'}
