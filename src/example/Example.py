class Example(object):
    
    def getExample():
        return "This is a response from the example get-API"

    def postExample(message=""):
        print("debug type: ",type(message), message)
        if message != "":
            return {
            "statusMessage":"This is a response from the example post-API, ",
            "message": "You sendt the following message: "+str(message)
            }
        else:
            return {
            "statusMessage":"This is a response from the example post-API, ",
            "message": 'You did not specify a “message”: in your json post'
            }