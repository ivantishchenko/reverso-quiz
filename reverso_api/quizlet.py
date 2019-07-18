import requests
import csv
import time
from requests.exceptions import HTTPError

class QuizletAPI:

    OUT_NAME = 'quiz.csv'
    SET_ID = '415417844'
    CREDENTIALS_FILE = 'credentials.txt'
    URL = 'https://api.quizlet.com/2.0/sets/' + SET_ID + '/terms'

    def __init__(self):
        pass

    def __readToken(self):
        with open(self.CREDENTIALS_FILE, encoding='utf-8') as f:
            read_data = f.read()
            return read_data
    
    def __postCard(self, term, definition):
        token = self.__readToken()
        headers = {'Authorization': 'Bearer '+ token}
        data = {'term':term, 'definition':definition}
        try:
            r = requests.post(self.URL, headers=headers, data=data)
            r.raise_for_status()
            time.sleep(.900)
            res = r.text
            print("Created a card...")
            print(res)
            return True
        except HTTPError as http_err:
            print("Error while posting a card...")
            print(r.status_code)
            return False
        

    def postMissingCards(self):
        print("Posting missing cards:")
        cache = []
        with open(self.OUT_NAME, 'r', newline="", encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            for i, line in enumerate(reader):
                if line[4] == '0':
                    if self.__postCard(line[1], line[2]):
                        line[4] = '1'
                cache.append(line)

        with open(self.OUT_NAME, 'w', newline="", encoding='utf-8') as csvfile:
            dict_writer = csv.writer(csvfile, delimiter=',')
            for line in cache:
                dict_writer.writerow(line)
                
# a = QuizletAPI()
# a.postMissingCards()