from peewee import MySQLDatabase, Model
from peewee import CharField, DateField, BooleanField, IntegerField, DateTimeField
db = MySQLDatabase('testdb', host = 'localhost', user = 'admin', passwd= '1234')

class BaseModel(Model): 
    class Meta: 
        database = db 

class Users(BaseModel): 
    username = CharField(verbose_name = 'Username', max_length = 15, primary_key = True)
    passwd = CharField(verbose_name = 'Password',max_length = 20)
    email = CharField(verbose_name = 'Email', max_length = 25)
    phone = CharField(verbose_name = 'Phone', max_length = 11, null = True)
    # created_time = DateField(verbose_name = 'Member since')
    # last_login_time=DateTimeField(verbose_name = 'Last login')

# print(db.is_closed())
# db.connect()
# print(db.is_closed())
# User.create_table()
# User.create(username = 'bunny', email = 'bunny@girlfriend.com', passwd = '1234')