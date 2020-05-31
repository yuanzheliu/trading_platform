from peewee import MySQLDatabase, Model
from peewee import CharField, DateField, BooleanField, IntegerField, DateTimeField

class BaseModel(Model): 
    class Meta: 
        database =  MySQLDatabase('testdb', host = 'localhost', user = 'admin', passwd= '1234')

class Users(BaseModel): 
    username = CharField(verbose_name = 'Username', max_length = 15, primary_key = True)
    passwd = CharField(verbose_name = 'Password',max_length = 20)
    email = CharField(verbose_name = 'Email', max_length = 25)
    phone = CharField(verbose_name = 'Phone', max_length = 11, null = True)
    # created_time = DateField(verbose_name = 'Member since')
    # last_login_time=DateTimeField(verbose_name = 'Last login')

def create_user(username, passwd,email,phone = None): 
    try:
        Users.create(username=username,passwd = passwd, email = email, phone = phone)
        return True
    except:
        return False

def create_all():
    '''
    Initialize database. This function should only be called once. 
    '''
    Users.create_table()

if __name__ == '__main__':
    create_all()
    print(create_user('bunny', '1234', 'heart@thomas'))
    a = Users.get(Users.username == 'bunny')
    print(a.email)
    print(create_user('bunny', '1234', 'heart@thomas'))
    a = Users.get(Users.username == 'bunny')
    print(a.email)
    # Users.create(username = 'bunny', email = 'bunny@girlfriend.com', passwd = '1234')

