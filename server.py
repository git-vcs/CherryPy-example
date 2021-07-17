from src.example.ExampleRouter import exampleRouter
from src.calculator.calculatorRouter import calculatorRouter
import cherrypy
import os
port = os.getenv('PORT', 'There is no port variable defined')
print("Heroku PORT:", port)
conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
            'server.socket_port': port
        }
    }

baseAPI="/api"

if __name__ == '__main__':
    exampleRouter(baseAPI,"/example",conf)
    calculatorRouter(baseAPI,"/calculator",conf)
    cherrypy.engine.block()
    
