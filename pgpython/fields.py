import json
import abc

class Storage:
	def __get__(self, obj, cls):
		return getattr(obj, self.name)

	def __set__(self, obj, value):
		setattr(obj, self.name, self)

class Validated(abc.ABC, Storage):
	def __set__(self, obj, value):
		value = self.validate(obj, value) 
		super().__set__(obj, value)

	@abc.abstractmethod
	def validate(self, instance, value):
		"""return validated value or raise ValueError"""

	@abc.abstractmethod
	def formatSQL(self):
		"""return value formated for SQL query"""

class StringField(Validated):
	def validate(self, instance, value):
		if type(value) is not str:
			raise ValueError(f"Parameter {self.name} must be string")

		self.value = value
		return self

	def formatSQL(self):
		return "'{0}'".format(self.value)

class JSONField(Validated):
	def validate(self, instance, value):
		self.value = value
		return self

	def formatSQL(self):
		return "'{0}'".format(json.dumps(self.value))

class IntegerField(Validated):
	def validate(self, instance, value):
		if type(value) is not int:
			raise ValueError(f"Parameter {self.name} must be int")

		self.value = value
		return self

	def formatSQL(self):
		return str(self.value)

class DateField(Validated):
	def validate(self, instance, value):
		self.value = value
		return self

	def formatSQL(self):
		return "TO_DATE('{0}','DD/MM/YYYY')".format(self.value)