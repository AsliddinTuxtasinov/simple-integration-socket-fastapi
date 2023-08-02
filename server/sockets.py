import socketio

sio_server = socketio.AsyncServer(
    async_mode='asgi',
    cors_allowed_origins=['*'],
)

sio_app = socketio.ASGIApp(
    socketio_server=sio_server,
    socketio_path='/socket'  # Use leading slash to avoid conflict with regular routes
)


@sio_server.event
async def connect(sid, environ, auth):
    print(f"{sid}: connected to socket sio_server -> in sockets.py")


@sio_server.event
async def disconnect(sid):
    print(f"{sid}: disconnect to socket sio_server -> in sockets.py")
