from Donnees.dataset import Dataset
from Donnees.donnees_covid import Covid 

class EstimationDescriptive:

    ''' Classe héritant de la classe Estimation. Elle permet d'effectuer des estimations descriptives sur un dataset, 
     notamment calculer une moyenne, une variance ou un écart-type.

     Examples
     ----------
     >>> d=Covid('./Donnees/Donnees_Covid/covid-hospit-incid-reg-2021-03-03-17h20.csv')
     >>> b=Vacance('./Donnees/vacances.json')
     >>> data= Dataset(d,b)
     >>> print(EstimationDescriptive().moyenne(data))

    '''

    def __init__(self):
        pass
        
    def moyenne(self,dataset):
        '''renvoie la moyenne de toutes les variables contenues dans le dataset 

        Parameters
        -----------
        dataset : Dataset

        Returns
        -----------
        dataset 
            contenant les moyennes et les nom des variables
        '''
        resu=[]
        largueur=len(dataset.donnees_covid.liste[0])
        longueur = len(dataset.donnees_covid.liste)-1
        for i in range(largueur):
            if type(dataset.donnees_covid.liste[1][i])==float:
                sum=0
                for donnees in dataset.donnees_covid.liste[1:]:
                    sum=sum +float(donnees[i])
                resu.append(['{}'.format(dataset.donnees_covid.liste[0][i]),sum/longueur])
        return Dataset(Covid(None,resu),dataset.donnees_vacances)

    def variance(self,dataset):
        '''renvoie la variance de toutes les variables contenues dans le dataset 

        Parameters
        -----------
        dataset : Dataset

        Returns
        -----------
        dataset 
            contenant les variances et les nom des variables
        '''
        resu=[]
        largueur=len(dataset.donnees_covid.liste[0])
        longueur = len(dataset.donnees_covid.liste)-1
        for i in range(largueur):
            if type(dataset.donnees_covid.liste[1][i])==float:
                var=0
                for j in range(len(self.moyenne(dataset).donnees_covid.liste)):
                    if self.moyenne(dataset).donnees_covid.liste[j][0]==dataset.donnees_covid.liste[0][i]:
                        indice= j

                
                moy=self.moyenne(dataset).donnees_covid.liste[indice][1]
                
        
                for donnees in dataset.donnees_covid.liste[1:]:
                    var= var+(float(donnees[i])-moy)**2
                resu.append(['{}'.format(dataset.donnees_covid.liste[0][i]),var/longueur])
        return Dataset(Covid(None,resu),dataset.donnees_vacances)

    def ecart_type(self,dataset):
        '''renvoie la moyenne de toutes les variables contenues dans le dataset 

        Parameters
        -----------
        dataset : Dataset

        Returns
        -----------
        dataset 
            contenant les moyennes et les nom des variables
        '''
        resu=[]
        var=self.variance(dataset).donnees_covid.liste
        for ligne in var:
            resu.append([ligne[0],ligne[1]**(0.5)])

        return Dataset(Covid(None,resu),None)


    

