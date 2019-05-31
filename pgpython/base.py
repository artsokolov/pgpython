from pgpython.pgdb import PGSql
from pgpython.fields import Validated

class Base(type):
	def __new__(cls, name, bases, attrs):
		for key, value in attrs.items():
			if isinstance(value, Validated):
				value.name = '_column#' + key

		attrs['__DBNAME__'] = name

		return super().__new__(cls, name, bases, attrs)


class BaseModel(metaclass=Base):
	def __init__(self):
		self._db = PGSql(type(self).__DBNAME__)

	def getColumns(self):
		columns = dict()

		for col, val in self.__dict__.items():
			if col.startswith('_column'):
				columns[col.split('#')[1]] = val
		
		return columns

	def add(self):
		columns = self.getColumns()
		self._db.add(columns)

	def update(self):
		old_data = self._db.selectById(self.id.value)
		new_data = self.getColumns()

		update_data = dict()
		update_data['id'] = self.id

		for col, obj in new_data.items():
			if obj.value != old_data[col]:
				update_data[col] = obj

		self._db.update(update_data)

	def getBy(self, data):
		result = self._db.select(data)

		if not result['values']:
			error_data = " and ".join([f"{col} = {val.value}" for col, val in data.items()])
			raise ValueError("Row with data ({0}) was not found in {1}".format(error_data, self._db.table))

		ret_data = []

		for value in result['values']:
			ret_data.append(dict(zip(result['columns'], value)))

		return ret_data

	def delete(self):
		self._db.delete(self)

	@classmethod
	def loadById(cls, idx):
		cls.instance = cls.__new__(cls)
		cls.instance.__init__()

		cls.instance.id = idx

		result = cls.instance.getBy({'id': cls.instance.id})[0]

		for col, val in result.items():
			setattr(cls.instance, col, val)

		return cls.instance

	def __getattr__(self, name):
		return f"Атрибут {name} не был найден"