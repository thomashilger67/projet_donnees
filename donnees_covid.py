import csv

class Covid:

    ''' importe les données Covid et les transforme en dictionnnaire

    
    Parameters
    ----------

    jeu_de_donnees : str
        chemin d'accès aux fichiers csv

    Attributs 
    ---------

    jeu_de_donnees : str
        chemin d'accès aux fichiers csv

    Example 
    -------

    >>> a = Covid('./Donnees/Donnees_Covid/covid-hospit-incid-reg-2021-03-03-17h20.csv')
    >>> print(a.dictionnaire)
    >>> d = { Date : '2020-09-23', Région : 'Occitanie', NumRégion : '76', TauxIncidRea : '10' }  

    '''



    def __init__(self, jeu_de_donnee=None,jeu_de_donnee2=None,jeu_de_donnee_format_liste=None):
        self.jeu_de_donnee = jeu_de_donnee
        self.jeu_de_donnee2= jeu_de_donnee2
        self.jeu_de_donnee_format_liste=jeu_de_donnee_format_liste

        if not self.jeu_de_donnee_format_liste:
            data = []
            with open(jeu_de_donnee, encoding='ISO-8859-1') as csvfile :
                covidreader = csv.reader(csvfile,delimiter=';') 
                for row in covidreader :
                    data.append(row)
            
            
            for ligne in data:
                for i in range(len(data[0])):
                    try :
                        ligne[i]=float(ligne[i])
                    except :
                        pass
            self.liste = data

        else:
            self.liste= self.jeu_de_donnee_format_liste

                
        

        

    def __str__(self):
        for liste in self.liste : 
            print(liste)
    
    