import uvicorn
from fastapi import FastAPI
from sockets import sio_app

app = FastAPI()
app.mount(path="/", app=sio_app)


@app.get("/index")
async def home():
    return {'message': 'Hello guys'}


if __name__ == "__main__":
    uvicorn.run(app='main:app', reload=True)
