from donnees_Covid import Covid
from donnees_Vacances import Vacance

class Dataset:

     ''' crée un type de données regroupant les données Covid et Vacance

    
    Parameters
    _________

    donnees_covid : Covid
        données Covid du Dataset
    
    donnees_vacances : Vacance
        données Vacance du Dataset

    Attributs 
    _________

    __donnees_covid : Covid
        données Covid du Dataset
    
    __donnees_vacances : Vacance
        données Vacance du Dataset

    Example 
    _______

    >>> d = Dataset(Covid('./Données/Données Covid/covid-hospit-incid-reg-2021-03-03-17h20.csv'),Vacance('./Données/vacances.json'))
    >>> print(d)
    >>>

    '''



    def __init__(self,donnees_covid,donnees_vacances=None):
        self.__donnees_covid=donnees_covid
        self.__donnees_vacances=donnees_vacances

    def ajout_donnees_covid(self,new_donnee,position=-1): #la première position doit ici correspondre à 0
        if position==-1:
            self.__donnees_covid.append(new_donnee)
        else:
            self.__donnees_covid.insert(position,new_donnee)
    
    def suppr_donnees_covid(self,position=-1):
        del(self.__donnees_covid[position])


    


