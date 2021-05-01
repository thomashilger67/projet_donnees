import csv

class Covid:

    ''' importe les données Covid et les transforme en dictionnnaire

    
    Parameters
    _________

    jeu_de_donnees : str
        chemin d'accès aux fichiers csv

    Attributs 
    _________

    jeu_de_donnees : str
        chemin d'accès aux fichiers csv

    Example 
    _______

    >>> a = Covid('./Donnees/Donnees_Covid/covid-hospit-incid-reg-2021-03-03-17h20.csv')
    >>> print(a.dictionnaire)
    >>> d = { Date : '2020-09-23', Région : 'Occitanie', NumRégion : '76', TauxIncidRea : '10' }  

    '''



    def __init__(self, jeu_de_donnee):
        self.jeu_de_donnee = jeu_de_donnee
        data = []
        with open(jeu_de_donnee, encoding='ISO-8859-1') as csvfile :
            covidreader = csv.reader(csvfile, delimiter=';') 
            for row in covidreader :
                data.append(row)
        self.dictionnaire = data
    