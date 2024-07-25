from peewee import Model, CharField, ForeignKeyField


from settings import postgres_database


class BaseModel(Model):
    """A base model that will use our Postgresql database"""

    class Meta:
        database = postgres_database


class ApiUser(BaseModel):
    """
    Model representing an API user.

    Attributes:
        name (CharField): The name of the user.
        email (CharField): The user's email address (unique).
        password (CharField): The user's password (unique).
    """

    name = CharField()
    email = CharField(unique=True)
    password = CharField(unique=True)


class Location(BaseModel):
    """
    Model representing a location.

    Attributes:
        name (CharField): The name of the location.
    """

    name = CharField()


class Device(BaseModel):
    """
    Model representing a device.

    Attributes:
        name (CharField): The name of the device.
        type (CharField): The type of the device.
        login (CharField): The login credentials for the device.
        password (CharField): The password for the device (unique).
        location (ForeignKeyField): The location of the device (foreign key to Location).
        api_user (ForeignKeyField): The API user associated with the device (foreign key to ApiUser).
    """

    name = CharField()
    type = CharField()
    login = CharField()
    password = CharField(unique=True)
    location = ForeignKeyField(related_name="devices", model=Location, null=True)
    api_user = ForeignKeyField(related_name="devices", model=ApiUser, null=True)
