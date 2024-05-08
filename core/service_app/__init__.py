import os

from fastapi import FastAPI

app = FastAPI(
    title="algo_runner",
    version="1.0.0",
    description="Algo runner micro",
    openapi_url="/openapi.json",
    debug=True,
    docs_url=None,
    redoc_url=None
)


@app.get("/")
async def running():
    return "<p>Server is running  ...  see <a href='/docs'>/docs for more info</a></p>"


@app.get("/health")
async def health():
    return 200


@app.on_event("startup")
async def startup_event():
    with open('./.static/resources/banner.txt', 'r') as f:
        print(f.read())


@app.on_event("shutdown")
async def shutdown_event():
    print("... shutdown")
