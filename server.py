import json
import sys
import tornado.web
import tornado.ioloop
sys.path.append('/src')
from sql_models import Users

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



class AjaxHandler(BaseHandler):
    def post(self):
        print("Post data received")
        
        
        self.write(s)
        

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/test/", AjaxHandler),
    ])

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()