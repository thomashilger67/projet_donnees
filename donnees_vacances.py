import json 

class Vacance:

    '''importe les données Vacance et les transforme en dictionnnaire

     Parameters
    _________

    jeu_de_donnees : str
        chemin d'accès aux fichiers csv

    Attributs 
    _________

    dictionnaire : dictionnaire
        dictionnaire décrivant l'ensemble de l'objet Vacances

    Example 
    _______

    >>> b=Vacance('./Données/vacances.json')
    >>> print(b.dictionnaire)
    >>> {'id': 917, 'Description': 'Vacances de Carnaval', 'DateDebut': 'samedi 23 février 2019', 'DateFin': 'lundi 11 mars 2019', 'Zone': 'Guyane', 'annee_scolaire': '2018-2019', 'Debut': '2019-02-23', 'Fin': '2019-03-11'}
    '''


    def __init__(self, jeu_de_donnee):
        '''
        Création d'un objet Vacances

        Parameters 
        -----------
        jeu_de_donnee : str
            chemin d'accès au fichier json
        
        '''
        self.jeu_de_donnee=jeu_de_donnee
        data = []
        with open (jeu_de_donnee) as json_file:
            data  = json.load(json_file)
        self.dictionnaire=data 


        