import asyncio

from fastapi import FastAPI, Response

from src.main import main

app = FastAPI()


@app.get("/api/ring/")
async def ring(times=0, hour_times=0, volume=0.2):
    try:
        asyncio.create_task(main(int(times), int(hour_times), float(volume)))
    except Exception as e:
        print(e)
        return Response(content=str(e), status_code=500)
    return Response(status_code=200)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
