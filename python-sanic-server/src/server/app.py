import os.path
import socketio

from sanic import Sanic
from sanic.response import json


def get_app(r):

    app = Sanic("x_x")

    sio = socketio.AsyncServer(async_mode='sanic')

    sio.attach(app)

    @app.listener('before_server_start')
    async def setup_background(app, loop):
        # app.add_task(background(sio))
        pass

    @app.route("/lmk/status")
    def status(request):
        return json({"status": "ok"})

    @app.route("/lmk/ping")
    def ping(request):
        return json({"ping": "pong"})

    @sio.on("connect")
    async def connect(sid, environ):
        print("connect ", sid)

    @sio.event
    async def disconnect(sid):
        print("disconnect ", sid)

    @sio.event
    async def update(sid, data):
        print("update ", data)
        await sio.emit("update", {"weom": "meow"})

    dirname = os.path.join(
        os.path.dirname(__file__),
        "static",
    )

    app.static('/static', dirname)

    return app
