from pgpython import BaseModel

class SchemaMeta(type):
	def __new__(cls, name, bases, attrs):
		for attr, val in attrs.items():
			if isinstance(val, BaseModel):
				type(val).__DBNAME__ = name + '.' + type(val).__DBNAME__
				val._db.table = type(val).__DBNAME__

		return super().__new__(cls, name, bases, attrs)

class BaseSchema(metaclass=SchemaMeta):
	pass