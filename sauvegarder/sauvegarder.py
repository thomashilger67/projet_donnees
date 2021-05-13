from Donnees.dataset import Dataset
import csv
import json 

class Sauvegarder:
    '''classe qui permet de sauver nos résultats sur les données du Covid dans un fichier csv

    Parameters
    ----------
    donnees_a_sauvgarder : dataset

    Attributs
    ---------
    donnees_a_sauvgarder : dataset

    Examples
    ---------
    >>> a=Dataset(Covid('./Donnees/Donnees_Covid/donnees-hospitalieres-covid19-2021-03-03-17h03.csv'))
    >>> Sauvegarder(a).SauvegarderCSV('exemple')
    '''

    def __init__(self,donnees_a_sauvgarder):
        self.donnees_a_sauvgarder=donnees_a_sauvgarder

    def SauvegarderCSV(self,nom_du_fichier):
        ''' fonction qui sauve en csv nos résultats covid

        Parameters
        --------
        nom_du_fichier : str

        Returns 
        ---------
        csv

        Examples
        ---------
        >>> a=Dataset(Covid('./Donnees/Donnees_Covid/donnees-hospitalieres-covid19-2021-03-03-17h03.csv'))
        >>> Sauvegarder(a).SauvegarderCSV('exemple')
        '''
    

        with open('{}.csv'.format(nom_du_fichier), 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC,delimiter=';')
            writer.writerows(self.donnees_a_sauvgarder.donnees_covid.liste)
 
