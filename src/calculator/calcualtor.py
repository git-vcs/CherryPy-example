from random import *

class Calculator(object):
    questionMessage = "What do you get when you take "
    questionDik={
        "0":{
            "number01":"1",
            "number02":"2",
            "operator":"+"
        },
        "1":{
            "number01":"2",
            "number02":"1",
            "operator":"-"
        },
        "2":{
            "number01":"3",
            "number02":"5",
            "operator":"*"
        },
        "3":{
            "number01":"12.0",
            "number02":"2.0",
            "operator":"/"
        }
    }

    def getRandomeQuestion(self):
        keys = list(self.questionDik.keys())
        questionNumber = str(randint(0,len(keys)-1))
        print("Keys:", keys)
        oneQuestion = self.questionDik.get(questionNumber)       
        print(oneQuestion)
        outputQuestion = self.questionMessage + oneQuestion.get("number01")+" "+oneQuestion.get("operator")+" "+oneQuestion.get("number02")+"?"
        print(outputQuestion,questionNumber)
        return{"question":outputQuestion,"questionNumber":questionNumber}
    


    def calculate(self, number01, operator, number02):
        print(number01,operator,number02)
        if operator == "+":
            return int(number01) + int(number02)
        elif operator == "-":
            return int(number01) - int(number02)
        elif operator == "*":
            return int(number01) * int(number02)
        elif operator == "/":
            if number02 == "0": return "you can't divide by zero (╯°□°）╯︵ ┻━┻"
            return float(number01) / float(number02)

        return "calculation error"



    def checkAnswer(self,questionNumber="",answer="")->dict:
        if questionNumber == "" or answer == "":
            return {
            "message": "did you forget to post the questionNumber or answer"
            }
        else:
            question = self.questionDik.get(str(questionNumber))
            calculatedAnswer = self.calculate(question['number01'],question['operator'],question['number02'])
            print(calculatedAnswer,answer)
            if str(calculatedAnswer) == str(answer):
                return {
                        "message": "correct"
                        }
            else: 
                return {
                        "message": "wrong answer please try again"
                        }
