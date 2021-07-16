import cherrypy
from src.example.Example import Example
@cherrypy.expose
@cherrypy.tools.json_in(debug=True)
@cherrypy.tools.json_out(debug=True)
class exampleRouter():
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
            return   {"message": Example.getExample()}
        except (Exception) as error:
            print("Error:",error)
            return "errror"
            
        

    def POST(self):
        print("router: post")
        print(cherrypy.request.json)
        try:
            return Example.postExample(cherrypy.request.json['message'])
        except:
            return Example.postExample()

            


