import cherrypy
import time


@cherrypy.expose
class helloRouter():
    start = time.time()
    baseAPI = ""
    endPoint = ""
    conf = ""
    couter = 0

    def __init__(self, baseAPI, endPoint, conf):
        self.baseAPI = baseAPI
        self.endPoint = endPoint
        self.conf = conf
        cherrypy.tree.mount(self, baseAPI + endPoint, conf)
        cherrypy.engine.start()

    def GET(self):
        try:
            self.couter += 1
            print("router: get")
            res = "Hello World\nServer uptime: " + str(int(time.time() - self.start)) + " s.\nvisitors counter: " + str(
                self.couter)
            return res
        except (Exception) as error:
            print("Error:", error)
            return "errror"
