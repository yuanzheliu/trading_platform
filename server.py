import os
import json
import sys
import tornado.web
import tornado.ioloop
sys.path.append('/src')
from src.sql_models import create_all, create_user

class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Access-Control-Max-Age', 1000)
        #self.set_header('Content-type', 'application/json')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Allow-Headers',#'*')
                        'authorization, Authorization, Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, Access-Control-Allow-Methods')

class MainHandler(BaseHandler):
    def get(self):
        self.render("home.html")



class SignUpHandler(BaseHandler):
    def post(self):
        print("Sign up data received")
        args = json.loads(self.request.body)
        result = None
        if create_user(**args): 
            result = json.dumps({"status" : True})
        else:
            result = json.dumps({"status" : False})
        self.write(result)

class SignUpPageHandler(BaseHandler):
    def get(self):
        self.render("pages/sign_up.html")
        
settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "scripts")}

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"sign_up.html",SignUpPageHandler),
    (r"/signup/", SignUpHandler),
    ], ** settings)





if __name__ == '__main__':
    application.listen(8888)
    create_all()
    tornado.ioloop.IOLoop.instance().start()