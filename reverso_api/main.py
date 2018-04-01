import quizlet as cards
import reverso as dict

d = dict.DictionaryAPI()
c = cards.QuizletAPI()

d.buildCSV()
c.postMissingCards()