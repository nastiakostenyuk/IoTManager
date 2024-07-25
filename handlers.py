from aiohttp import web
from loguru import logger
from pydantic import ValidationError
from aiohttp.web import Request, Response
from peewee import DoesNotExist, IntegrityError


from schemas import DeviceModel
from models import Device as DeviceTable


class DeviceHandler:
    device_table = DeviceTable

    async def get_all(self, request: Request) -> Response:
        """Get all devices."""
        devices = self.device_table.select()
        return web.json_response({'devices': [device.to_dict() for device in devices]})

    async def get_by_id(self, request: Request) -> Response:
        """Get device by id."""
        device_id = request.match_info.get('id')
        try:
            device = self.device_table.get_by_id(pk=device_id)
            return web.json_response(device.__data__, status=200)
        except DoesNotExist:
            return web.HTTPNotFound(text=f'Device with id {device_id} not found')
        except Exception as exp:
            logger.exception(f"An unexpected error occurred: {exp}")
            return web.json_response({'error': 'Internal server error'}, status=500)

    async def create(self, request: Request) -> Response:
        """Create new device."""
        data = await request.json()  # request in json formate
        try:
            # validate data using pydantic model
            DeviceModel(**data)
            device = self.device_table.create(**data)
            return web.json_response({"id": device.id}, status=201)
        except ValidationError as e:
            return web.json_response({'errors': e.errors()}, status=400)
        except IntegrityError as e:
            return web.json_response({'errors': str(e)}, status=400)
        except Exception as exp:
            logger.exception(f"An unexpected error occurred: {exp}")
            return web.json_response({'error': 'Internal server error'}, status=500)

    async def delete(self, request: Request) -> Response:
        """Delete device."""
        print(request.match_info)
        device_id = int(request.match_info.get('id', -1))
        try:
            device = self.device_table.get_by_id(pk=device_id)
            device.delete_instance()
            return web.Response(status=204)
        except DoesNotExist:
            return web.HTTPNotFound(text=f'Device with id {device_id} not found')
        except Exception as exp:
            logger.exception(f"An unexpected error occurred: {exp}")
            return web.json_response({'error': 'Internal server error'}, status=500)

