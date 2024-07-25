from aiohttp import web
from loguru import logger

from handlers import DeviceHandler
from settings import postgres_database
from models import Device, ApiUser, Location


def create_app() -> web.Application:
    """
    Creates tables for models in the database (if they don't exist already).
    Create a new aiohttp application instance.
    """

    postgres_database.create_tables([Location, ApiUser, Device], safe=True)
    device_handler = DeviceHandler()
    app = web.Application()
    app.add_routes(
        [
            web.get("/api/devices/", device_handler.get_all),
            web.get("/api/devices/{id}/", device_handler.get_by_id),
            web.post("/api/devices/", device_handler.create),
            web.delete("/api/devices/{id}/", device_handler.delete),
            web.put("/api/devices/{id}/", device_handler.update),
        ]
    )
    return app


if __name__ == "__main__":
    try:
        logger.info(f"Run app")
        app = create_app()
        web.run_app(app)
    except KeyboardInterrupt:
        logger.info("Server stopped manually.")
    except Exception as e:
        logger.exception(e)
