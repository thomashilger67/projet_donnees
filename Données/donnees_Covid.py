import csv

class Covid():
    def __init__(self, jeu_de_donnee):
        self.jeu_de_donnee = jeu_de_donnee
        data = []
        with open(jeu_de_donnee, encoding='ISO-8859-1') as csvfile :
            covidreader = csv.reader(csvfile, delimiter=';') 
            for row in covidreader :
                data.append(row)
        self.dictionnaire = data
    