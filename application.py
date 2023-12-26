from fastapi import FastAPI
import uvicorn

application = FastAPI()

@application.get("/")
def read_root():
    return {"Hello": "World"}

