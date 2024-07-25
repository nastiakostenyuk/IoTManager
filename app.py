from aiohttp import web

from handlers import DeviceHandler
from settings import postgres_database
from models import Device, ApiUser, Location


def create_app() -> web.Application:
    postgres_database.create_tables([Location, ApiUser, Device], safe=True)
    device_handler = DeviceHandler()
    app = web.Application()
    app.add_routes([
        web.get("/api/devices", device_handler.get_all),
        web.get("/api/devices/{id}/", device_handler.get_by_id),
        web.post("/api/devices", device_handler.create),
        web.post("/api/devices/{id}/", device_handler.delete)
    ])
    return app


if __name__ == "__main__":
    app = create_app()
    web.run_app(app)
