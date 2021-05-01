import json 

class Vacance:

    '''importe les données Vacance et les transforme en dictionnnaire

     Parameters
    _________

    jeu_de_donnees : str
        chemin d'accès aux fichiers csv

    Attributs 
    _________

    jeu_de_donnees : str
        chemin d'accès aux fichiers json

    Example 
    _______

    >>> b=Vacance('./Données/vacances.json')
    >>> print(b.dictionnaire)
    >>> {'id': 917, 'Description': 'Vacances de Carnaval', 'DateDebut': 'samedi 23 février 2019', 'DateFin': 'lundi 11 mars 2019', 'Zone': 'Guyane', 'annee_scolaire': '2018-2019', 'Debut': '2019-02-23', 'Fin': '2019-03-11'}
    '''


    def __init__(self, jeu_de_donnee):
        self.jeu_de_donnee=jeu_de_donnee
        data = []
        with open (jeu_de_donnee) as json_file:
            data  = json.load(json_file)
        self.dictionnaire=data 


        