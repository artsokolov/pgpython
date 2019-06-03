## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pgpython.

```bash
pip install pgpython
```

## Usage 

### Connect to database

To connect to the database you must create .env file in your directory with needed variables. Example:

```python
DB_NAME=testdb
DB_USER=c0nder
DB_HOST=localhost
DB_PASSWORD=yourpassword
DB_PORT=5432
```

And that's all you need to do!

### Working with tables

Next we are going to deal with tables. Imagine that you have got a table called **users** with next columns:
  1. id (integer)
  2. username (text)

First, you have to import pgpython BaseModel to inherit your classes from it. Code:

```python
from pgpython import BaseModel
```

Next, you must import fields that you will use in your code. Fields must match up with you column type. Example:

```python
from pgpython.fields import IntegerField, StringField
```

There are 4 types in total: **IntegerField, DateField, JSONField, StringField**

Next, you must create a class called as your table name with attributes called as your columns. Code:

```python
class users(BaseModel):
  id = IntegerField()
  username = StringField()
```

That's is all you need to tie up your class and table.

### methods

#### Insert data

After creating a class you must create an object of this class. Using our example of users table let's code:


```python
user = users()
```

Next, let's set our data to an object.

**IMPORTANT** If you have an auto_incremented id than you must not to set id to your object.


```python
user.id = 1
user.username = 'c0nder'
```

Then, use method add()

```python
user.add()
```

That's all!

#### Selecting data from table

At first, you must, as always, create an object and set data that you need to use to select data from table. Than use method select() to select data.

```python
user = users()
user.username = 'c0nder'
data = user.select({'username': user.username})
```

#### Load object by id

```python
user = users.loadById(1)
```

#### Updating data

```python
user = users.loadById(1)
user.username = 'New_username'
user.update()
```

#### Delete data

```python
user = users.loadById(1)
user.delete()
```

#### Getting columns of table object


```python
user = users.loadById(1)
columns = user.getColumns()

for col, obj in columns.items():
	print(col, ":", obj.value)
```

#### Printing value of object attribute

```python
user = users.loadById(1)
print(user.username.value)
```

### Working with Schemas

To work with schemas you need to import BaseSchema.

```python
from pgpython import BaseModel, BaseSchema
```

Next, we will use our table users.

```python
class users(BaseModel):
  id = IntegerField()
  username = StringField()
```

Than, you need to create schema class.

```python
class schema_name(BaseSchema):
  users = users()
```
Example of using:

```python
user = schema_name.loadById(1)
```

That's all!
>>>>>>> Added ReadMe
