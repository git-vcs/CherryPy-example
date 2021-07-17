from src.example.ExampleRouter import exampleRouter
from src.calculator.calculatorRouter import calculatorRouter
from src.Hello import helloRouter
import cherrypy
import os
port = int(os.getenv('PORT', '8080'))
print("PORT: ", port)
# checing is the program in running on heroku
autoReload = False if  os.getenv('FORWARDED_ALLOW_IPS') else True
print("AUTORELOAD: ", autoReload)

# for pining all env

# for item, value in os.environ.items():
#    print('{}: {}'.format(item, value))

conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')]
        }
    }
   

baseAPI = "/api"
globalConf = {
            'server.socket_port': port,
            'server.socket_host': '0.0.0.0',
            'engine.autoreload.on':autoReload
            }

if __name__ == '__main__':
    cherrypy.config.update(globalConf)
    helloRouter("/", "", conf)
    exampleRouter(baseAPI,"/example", conf)
    calculatorRouter(baseAPI,"/calculator", conf)
    cherrypy.engine.block()