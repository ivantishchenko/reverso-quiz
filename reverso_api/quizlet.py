import requests

class QuizletAPI:

    SET_ID = '282592606'
    CREDENTIALS_FILE = 'credentials.txt'
    URL = 'https://api.quizlet.com/2.0/sets/' + SET_ID + '/terms'

    def __init__(self):
        pass

    def readToken(self):
        with open(self.CREDENTIALS_FILE) as f:
            read_data = f.read()
            return read_data
    
    def postCard(self, term, definition):
        token = self.readToken()
        headers = {'Authorization': 'Bearer '+ token}
        data = {'term':term, 'definition':definition}
        r = requests.post(self.URL, headers=headers, data=data)
        res = r.text
        print(res)

a = QuizletAPI()
a.postCard("hello", "wolrd")