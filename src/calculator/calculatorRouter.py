import cherrypy
from src.calculator.calcualtor import Calculator


@cherrypy.expose
@cherrypy.tools.json_in(debug=False)
@cherrypy.tools.json_out(debug=False)
class calculatorRouter():
    calcualtor = Calculator()
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
            print("router: get")
            oneQuestion = self.calcualtor.getRandomeQuestion()
            return {
                "title": "This is a simple calculator backend-game, please answer the follow question by posting the answer: and questionNumber:",
                "question": oneQuestion["question"],
                "questionNumber": oneQuestion["questionNumber"]
            }

        except (Exception) as error:
            print("Error:", error)
            return "errror"

    def POST(self, name=""):
        print(cherrypy.request.json)
        if name == "calculate":
            try:
                return {"answer": self.calcualtor.calculate(
                    cherrypy.request.json['number01'],
                    cherrypy.request.json['operator'],
                    cherrypy.request.json['number02'], )
                }
            except (Exception) as error:
                print("error", error)
                return {"error": "You are probably missing number01, operator or number02 in your json"}

        try:
            return self.calcualtor.checkAnswer(cherrypy.request.json.get('questionNumber'),
                                               cherrypy.request.json.get('answer'))
        except (Exception) as error:
            print("error", error)
            return self.calcualtor.checkAnswer()
