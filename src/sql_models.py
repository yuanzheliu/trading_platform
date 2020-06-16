from peewee import MySQLDatabase, Model
from peewee import CharField, DateField, BooleanField, IntegerField, DateTimeField

class BaseModel(Model): 
    class Meta: 
        database =  MySQLDatabase('testdb', host = 'localhost', user = 'admin', passwd= '1234')

class Users(BaseModel): 
    username = CharField(verbose_name = 'Username', max_length = 15, primary_key = True)
    password = CharField(verbose_name = 'Password',max_length = 20)
    email = CharField(verbose_name = 'Email', max_length = 25)
    phone = CharField(verbose_name = 'Phone', max_length = 11, null = True)
    # created_time = DateField(verbose_name = 'Member since')
    # last_login_time=DateTimeField(verbose_name = 'Last login')

class Books(BaseModel):
    title = CharField(verbose_name = 'Title', max_length = 30, primary_key = True)
    price = FloatField(verbose_name = 'Price',constraints=[Check('price > 0')])
    year = IntegerField(verbose_name= 'Year')
    author = CharField(verbose_name = 'Author')
    category = CharField(verbose_name= 'Category')
    stock = IntegerField(Verbose_name = 'Stock')
    publisher = CharField(verbose_name = 'Publisher')

def create_user(username, password,email,phone = None): 
    try:
        Users.create(username=username,password = password, email = email, phone = phone)
        return True
    except:
        return False

def create_all():
    '''
    Initialize database. This function should only be called once. 
    '''
    try:
        Users.create_table()
    except:
        return


if __name__ == '__main__':
    create_all()
    print(create_user('bunny', '1234', 'heart@thomas'))
    a = Users.get(Users.username == 'bunny')
    print(a.email)
    print(create_user('bunny', '1234', 'heart@thomas'))
    a = Users.get(Users.username == 'bunny')
    print(a.email)
    # Users.create(username = 'bunny', email = 'bunny@girlfriend.com', passwd = '1234')

