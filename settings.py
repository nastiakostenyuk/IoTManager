import os
import sys

from loguru import logger
from dotenv import load_dotenv
from peewee import PostgresqlDatabase

load_dotenv()


postgres_database = PostgresqlDatabase(database=os.getenv("POSTGRES_DB"),
                                       user=os.getenv("POSTGRES_USER"),
                                       password=os.getenv("POSTGRES_PASSWORD"),
                                       host=os.getenv("POSTGRES_HOST"),
                                       port=os.getenv("POSTGRES_PORT"))

# Setting up logs
log_folder = "./logs"
os.makedirs(log_folder, exist_ok=True)
logger.add(sys.stdout, level="INFO")
logger.add(f"{log_folder}/file_{{time:DD-MM}}_{{time:HH-mm}}.log", rotation="100 MB", retention="1 day",
           format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")
