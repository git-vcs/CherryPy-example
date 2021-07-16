from src.example.ExampleRouter import exampleRouter
from src.calculator.calculatorRouter import calculatorRouter
import cherrypy
conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        }
    }

baseAPI="/api"

if __name__ == '__main__':
    exampleRouter(baseAPI,"/example",conf)
    calculatorRouter(baseAPI,"/calculator",conf)
    cherrypy.engine.block()
    
