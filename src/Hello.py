import cherrypy
from src.example.Example import Example
@cherrypy.expose
class helloRouter():
    baseAPI=""
    endPoint=""
    conf=""
    def __init__(self,baseAPI,endPoint,conf):
        self.baseAPI = baseAPI
        self.endPoint = endPoint
        self.conf = conf
        cherrypy.tree.mount(self,baseAPI+endPoint,conf)
        cherrypy.engine.start()

    def GET(self):
        try:
            print("router: get")
            return   "Hellow World"
        except (Exception) as error:
            print("Error:",error)
            return "errror"
            

            


