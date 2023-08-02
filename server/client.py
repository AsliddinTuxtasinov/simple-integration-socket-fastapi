import socketio
import asyncio

sio_client = socketio.AsyncClient()


@sio_client.event
async def connect():
    print(f"connected to sio client")


@sio_client.event
async def disconnect():
    print(f"disconnect to sio client")


async def main():
    await sio_client.connect(url="http://localhost:8000", socketio_path="/socket")
    await asyncio.sleep(5)  # Add some delay to see the messages printed
    await sio_client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
