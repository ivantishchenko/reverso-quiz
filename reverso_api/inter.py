import requests
import csv

class DictionaryAPI:
    OUT_NAME = "quiz.csv"
    WORD_LIMIT = 10000
    USER = "ivan.tishchenko"
    URL = "http://context.reverso.net/user-profile/user-public-favourites?mode=0&user_name="+USER+"&start=0&length=" + str(WORD_LIMIT) + "&options=&order[0][column]=5&order[0][dir]=desc"

    def __init__(self):
        print("Create the API object...")
        #print(self.URL)
    
    def getData(self):
        print("Getting the JSON data for a user " + self.USER + "...")
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
        r = requests.get(self.URL, headers=headers)
        res = r.json()
        return res
    
    def buildCSV(self):
        res = self.getData()
        dictonaryData = res['data']

        with open(self.OUT_NAME, 'w', newline="") as csvfile:
            dict_writer = csv.writer(csvfile, delimiter=',')
            for each_entry in dictonaryData:
                src = each_entry['srcText']
                trg = each_entry['trgText']
                context = each_entry['srcContext']

                context = context.replace('<em>', '*').replace('</em>', '*')
                src = "*" + src + "*"

                term = src + " - [" + context + "]"

                dict_writer.writerow([term, trg])
                #dict_writer.writerow([src + " - [" + context +"]", trg])




a = DictionaryAPI()
a.buildCSV()