from donnees_Covid import Covid
from donnees_Vacances import Vacance

class Dataset:

    ''' crée un type de données regroupant les données Covid et Vacance

    
    Parameters
    ----------

    donnees_covid : Covid
        données Covid du Dataset
    
    donnees_vacances : Vacance
        données Vacance du Dataset

    Attributs 
    ---------

    __donnees_covid : Covid
        données Covid du Dataset
    
    __donnees_vacances : Vacance
        données Vacance du Dataset

    Example 
    -------

    >>> d = Dataset(Covid('./Données/Données Covid/covid-hospit-incid-reg-2021-03-03-17h20.csv'),Vacance('./Données/vacances.json'))
    >>> print(d)
    >>>

    '''


    def __init__(self,donnees_covid,donnees_vacances=None):
        '''Construit un Dataset

        Parameters
        ----------
        donnees_covid : Covid
            données covid du dataset

        donnees_vacances : Point
            donnees_vacances du dataset

        Examples
        --------
        >>> d = Dataset(Covid('./Données/Données Covid/covid-hospit-incid-reg-2021-03-03-17h20.csv'),Vacance('./Données/vacances.json'))
        '''

        self.__donnees_covid=donnees_covid
        self.__donnees_vacances=donnees_vacances

    def ajout_donnees_covid(self,new_donnee,position=-1): #la première position doit ici correspondre à 0
        '''Ajoute une donné liée au Covid à donnees_covid

        Parameters
        ----------
        new_donnee : list
            nouvelle donnée à ajouter

        position : int
            position à laquelle est placée la nouvelle donnée dans la liste

        Examples
        --------
        >>> d = Dataset(Covid('./Données/Données Covid/covid-hospit-incid-reg-2021-03-03-17h20.csv'),Vacance('./Données/vacances.json'))
        >>> ajout_donnees_covid([2020-03-19;"Centre-Val de Loire";24;6])

        '''    
        
        if position==-1:
            self.__donnees_covid.append(new_donnee)
        else:
            self.__donnees_covid.insert(position,new_donnee)
    
    def suppr_donnees_covid(self,position=-1):

        '''Supprime une donné liée au Covid située à position 

        Parameters
        ----------
        position : int
            position à laquelle est placée la nouvelle donnée dans la liste

        Examples
        --------
        >>> d = Dataset(Covid('./Données/Données Covid/covid-hospit-incid-reg-2021-03-03-17h20.csv'),Vacance('./Données/vacances.json'))
        >>> suppr_donnees_covid([2020-03-19;"Centre-Val de Loire";24;6])

        '''    
        
        del(self.__donnees_covid[position])

    def ajout_donnees_vacances(self,cle,new_vac):

        '''Ajoute une donné liée au Vacance à donnees_vacances 

        Parameters
        ----------
        cle : str
            clé du dictionnaire (Calendrier/Académie)

        new_vac : dict
            nouvelle donnée à ajouter
        

        Examples
        --------
        >>> d = Dataset(Covid('./Données/Données Covid/covid-hospit-incid-reg-2021-03-03-17h20.csv'),Vacance('./Données/vacances.json'))
        >>> ajout_donnees_vacances("Calendrier",{"id":4,"Description":"Vacances d'Été","DateDebut":"lundi 09 juillet 2012","DateFin":"lundi 10 septembre 2012","Zone":"Corse","annee_scolaire":"2011-2012","Debut":"2012-07-09","Fin":"2012-09-10"})

        '''    
        
        l=self.__donnees_vacances.dictionnaire[cle]
        if new_vac['id']<len(l):
            l[new_vac['id']]=new_vac
        else :
            l.append(new_vac)
        d_bis={cle : l}
        self.__donnees_vacances.update(d_bis)
        
    def suppr_donnees_vacances(self,cle,id):
        '''Ajoute une donné liée au Vacance à donnees_vacances 

        Parameters
        ----------
        cle : str
            clé du dictionnaire (Calendrier/Académie)

        id : int
            identifiant de la donnée que l'on veut supprimer
        

        Examples
        --------
        >>> d = Dataset(Covid('./Données/Données Covid/covid-hospit-incid-reg-2021-03-03-17h20.csv'),Vacance('./Données/vacances.json'))
        >>> suppr_donnees_vacances("Calendrier",1048)

        '''    

        del((self.__donnees_vacances.dictionnaire[cle])[id])



    


