import csv

class Covid:
    ''' importe les données Covid et les transforment en liste

    
    Parameters
    ----------

    jeu_de_donnees : str
        chemin d'accès au fichier csv
    
    jeu_de_donnees_format_liste : list
        list que l'on veut transfomrer en objet Covid

    Attributs 
    ---------

    liste : list
        liste contenant les données 

    Example 
    -------

    >>> a = Covid('./Donnees/Donnees_Covid/covid-hospit-incid-reg-2021-03-03-17h20.csv')
    >>> print(a.list)
    [['jour', 'nomReg', 'numReg', 'incid_rea']... 
    '''



    def __init__(self, jeu_de_donnee=None,jeu_de_donnee_format_liste=None):
        '''
        construit un objet direct 

        Parameters
        -----------
        jeu_de_donnee : str
            chemin d'accès au fichier csv

        jeu_de_donnee_format_liste : liste
            liste à transformer en Covid

        '''
        if  jeu_de_donnee_format_liste is None:
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
            self.liste= jeu_de_donnee_format_liste     

        

    def __str__(self):
        '''Chaîne décrivant l'ensemble des données contenu dans Covid 

        Returns 
        ---------
        str 
            description de l'article 
        '''        
        return(str(self.liste))
    
    