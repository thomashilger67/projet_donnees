import json

class Vacance():

     ''' importe les données Vacances et les transforme en dictionnnaire

    Attributs 
    _________

    dico : dict
        dictionnaire initialement vide dans lequel on va stocker nos données

    jeu_de_donnees : str
        chemin d'accès aux fichiers json

    Example 
    _______

    >>>> a = Covid('./Données/Données Vacances/')
    >>>> print(a.dictionnaire)
    >>>> d = { Date : '2020-09-23', Région : 'Occitanie', NumRégion : '76', TauxIncidRea : '10' }  

    '''

    def __init__(self,jeu_de_donnee):
        self.jeu_de_donnee = jeu_de_donnee
        data=[]
        with open(jeu_de_donnee) as json_file :
            data = json.load(json_file)
        self.dictionnaire = data


