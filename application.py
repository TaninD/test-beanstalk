from fastapi import FastAPI
import uvicorn

application = FastAPI()


@application.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(application, host="0.0.0.0", port=5000)
