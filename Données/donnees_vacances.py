import json 

class Vacance():
    '''importe les données Vacance et les transforme en dictionnnaire

    Attributs 
    _________

    dico : dict
        dictionnaire initialement vide dans lequel on va stocker nos données

    jeu_de_donnees : str
        chemin d'accès aux fichiers json

    Example 

    ---------

    >>> b=Vacance('./Données/vacances.json')
    >>> print(b.dictionnaire)
    '''

    def __init__(self, jeu_de_donnee):
        self.jeu_de_donnee=jeu_de_donnee
        data = []
        with open (jeu_de_donnee) as json_file:
            data  = json.load(json_file)
        self.dictionnaire=data 