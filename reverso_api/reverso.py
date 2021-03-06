import requests
import csv

class DictionaryAPI:
    OUT_NAME = "quiz.csv"
    WORD_LIMIT = 10000
    USER = "ivan.tishchenko"
    URL = "http://context.reverso.net/user-profile/user-public-favourites?mode=0&user_name="+USER+"&start=0&length=" + str(WORD_LIMIT) + "&options=&order[0][column]=5&order[0][dir]=desc"

    def __init__(self):
        print("Create the API object...")
        self.__readCSVDictionary()
        #print(self.URL)
    
    def __readCSVDictionary(self):
        try:
            with open(self.OUT_NAME, encoding='utf-8') as f:
                # self.dict_content = [line.split() for line in f]
                # print(self.dict_content)
                self.dict_content = []
                reader = csv.reader(f, delimiter=",")
                for i, line in enumerate(reader):
                    self.dict_content.append(line)
        except IOError:
            print("Dictionary CSV doen't exist...")
            self.dict_content = []

    def __getData(self):
        print("Getting the JSON data for a user " + self.USER + "...")
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
        r = requests.get(self.URL, headers=headers)
        res = r.json()
        return res
    
    def __recordExists(self, src, trg):
        for i, line in enumerate(self.dict_content):
            if line[0] == src and line[2] == trg:
                return True
            # print("line{0} = {1}".format(i, line))
        return False

    def buildCSV(self):
        res = self.__getData()
        dictonaryData = res['data']

        with open(self.OUT_NAME, 'a', newline="", encoding='utf-8') as csvfile:
            dict_writer = csv.writer(csvfile, delimiter=',')
            for each_entry in dictonaryData:
                src = each_entry['srcText']
                trg = each_entry['trgText']
                context = each_entry['srcContext']
                date = each_entry['creationDate']

                if self.__recordExists(src, trg) == False:
                    context = context.replace('<em>', '*').replace('</em>', '*')
                    term = "*" + src + "*"
                    term = term + " - [" + context + "]"
                    dict_writer.writerow([src, term, trg, date, '0'])


# a = DictionaryAPI()
# a.buildCSV()