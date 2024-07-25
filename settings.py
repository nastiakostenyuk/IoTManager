import os

from aiohttp import web
from dotenv import load_dotenv
from peewee import PostgresqlDatabase

load_dotenv()


router = web.RouteTableDef()


postgres_database = PostgresqlDatabase(database=os.getenv("POSTGRES_DB"),
                                       user=os.getenv("POSTGRES_USER"),
                                       password=os.getenv("POSTGRES_PASSWORD"),
                                       host=os.getenv("POSTGRES_HOST"))
