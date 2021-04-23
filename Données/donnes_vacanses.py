import json

class Vacance():
    def __init__(self,jeu_de_donnee):
        self.jeu_de_donnee = jeu_de_donnee
        data=[]
        with open(jeu_de_donnee) as json_file :
            data = json.load(json_file)
        self.dictionnaire = data


