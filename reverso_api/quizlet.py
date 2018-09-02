import requests
import csv

class QuizletAPI:

    OUT_NAME = 'quiz.csv'
    SET_ID = '282592606'
    CREDENTIALS_FILE = 'credentials.txt'
    URL = 'https://api.quizlet.com/2.0/sets/' + SET_ID + '/terms'

    def __init__(self):
        pass

    def __readToken(self):
        with open(self.CREDENTIALS_FILE) as f:
            read_data = f.read()
            return read_data
    
    def __postCard(self, term, definition):
        token = self.__readToken()
        headers = {'Authorization': 'Bearer '+ token}
        data = {'term':term, 'definition':definition}
        r = requests.post(self.URL, headers=headers, data=data)
        res = r.text
        print("Created card...")
        print(res)

    def postMissingCards(self):
        print("Posting missing cards:")
        cache = []
        with open(self.OUT_NAME, 'r', newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            for i, line in enumerate(reader):
                if line[4] == '0':
                    self.__postCard(line[1], line[2])
                    line[4] = '1'
                cache.append(line)

        with open(self.OUT_NAME, 'w', newline="") as csvfile:
            dict_writer = csv.writer(csvfile, delimiter=',')
            for line in cache:
                dict_writer.writerow(line)
                
# a = QuizletAPI()
# a.postMissingCards()