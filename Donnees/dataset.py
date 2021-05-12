from Donnees.donnees_covid import Covid
from Donnees.donnees_vacances import Vacance

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

    donnees_covid : Covid
        données Covid du Dataset
    
    donnees_vacances : Vacance
        données Vacance du Dataset

    Example 
    -------

    >>> d = Dataset(Covid('./Donnees/Donnees_Covid/covid-hospit-incid-reg-2021-03-03-17h20.csv'),Vacance('./Donnees/vacances.json'))
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

        self.donnees_covid=donnees_covid
        self.donnees_vacances=donnees_vacances

    def ajout_donnees_covid(self,new_donnee,position=-1): #la première position doit ici correspondre à 0
        '''Ajoute une donnée liée au Covid à donnees_covid

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
            
            self.donnees_covid.liste.append(new_donnee)
        else:
            self.donnees_covid.liste.insert(position,new_donnee)
    
    def suppr_donnees_covid(self,position=-1):

        ''' Supprime une donnée liée au Covid à donnees_covid

        Parameters
        ----------
        
        position : int
            position à laquelle on veut supprimer la donnée dans la liste

        Examples
        --------
        >>> d = Dataset(Covid('./Données/Données Covid/covid-hospit-incid-reg-2021-03-03-17h20.csv'),Vacance('./Données/vacances.json'))
        >>> suppr_donnees_covid()

        '''    

        del(self.donnees_covid.liste[position])

    def ajout_donnees_vacances(self,cle,new_vac):
        '''Ajoute une donnée liée au Covid à donnees_covid

        Parameters
        ----------

        cle : str
            clé où l'on veut placer la donnée (Calendrier/Academie)

        new_vac : list
            nouvelle donnée à ajouter

        Examples
        --------
        >>> d = Dataset(Covid('./Données/Données Covid/covid-hospit-incid-reg-2021-03-03-17h20.csv'),Vacance('./Données/vacances.json'))
        >>> ajout_donnees_vacances('Calendrier',{'id': 1, 'Description': "Vacances d'Hiver", 'DateDebut': 'lundi 22 fÃ©vrier 2010', 'DateFin': 'lundi 08 mars 2010', 'Zone': 'Corse', 'annee_scolaire': '2009-2010', 'Debut': '2010-02-22', 'Fin': '2010-03-08'})

        '''    

        self.donnees_vacances[cle].append(new_vac)
        
    def suppr_donnees_vacances(self,cle,id):

        ''' Supprime une donnée liée au Covid à donnees_covid

        Parameters
        ----------
        
        cle : str
            clé on l'où vont supprimer la donnée
        
        id : int
            identifiant que l'on veut supprimer

        Examples
        --------
        >>> d = Dataset(Covid('./Données/Données Covid/covid-hospit-incid-reg-2021-03-03-17h20.csv'),Vacance('./Données/vacances.json'))
        >>> suppr_donnees_vacances('Calendrier',1)

        '''   

        del((self.donnees_vacances[cle])[id])

    def __str__(self):
        ''' renvoie une chaîne de caractère qui décrit l'ensemble du contenu du Dataset

        Returns 
        ---------
        str
            description du dataset
        
        '''

        modele = '\n'.join(["les données Covid sont : {}","les données des vacances sont : {}"])
        return modele.format(self.donnees_covid.liste[0],self.donnees_vacances)



    


