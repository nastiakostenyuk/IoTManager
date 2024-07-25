from peewee import Model, CharField, ForeignKeyField


from settings import postgres_database


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = postgres_database


class ApiUser(BaseModel):
    name = CharField()
    email = CharField(unique=True)
    password = CharField(unique=True)


class Location(BaseModel):
    name = CharField()


class Device(BaseModel):
    name = CharField()
    type = CharField()
    login = CharField()
    password = CharField(unique=True)
    location = ForeignKeyField(related_name='devices', model=Location, null=True)
    api_user = ForeignKeyField(related_name='devices', model=ApiUser, null=True)



