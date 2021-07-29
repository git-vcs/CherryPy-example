import cherrypy
from src.status.status import Status


@cherrypy.expose
class statusRouter():
    status = Status()
    baseAPI = ""
    endPoint = ""
    conf = ""

    def __init__(self, baseAPI, endPoint, conf):
        self.baseAPI = baseAPI
        self.endPoint = endPoint
        self.conf = conf
        cherrypy.tree.mount(self, baseAPI + endPoint, conf)
        cherrypy.engine.start()

    def GET(self):
        try:
            # for debug
            print("router: status")
            return self.status.status()


        except (Exception) as error:
            print("Error:", error)
            return "errror"
