import asyncio

from fastapi import FastAPI, Response

from src.main import main

app = FastAPI()


@app.get("/api/ring/")
def hello(times=0, hour_times=0):
    asyncio.run(main)(times, hour_times)
    return Response(status_code=200)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
