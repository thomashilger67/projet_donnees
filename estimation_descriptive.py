from estimation import Estimation
from dataset import Dataset

class EstimationDescriptive(Estimation):
    def __init__(self):
        pass
        
    def moyenne(self,dataset):
        resu=[]
        largueur=len(dataset.donnees_covid.liste[0])
        longueur = len(dataset.donnees_covid.liste)-1
        for i in range(largueur):
            if type(dataset.donnees_covid.liste[1][i])==float:
                sum=0
                for donnees in dataset.donnees_covid.liste[1:]:
                    sum=sum +float(donnees[i])
                resu.append(['{}'.format(dataset.donnees_covid.liste[0][i]),sum/longueur])
        return resu 

    def variance(self,dataset):
        resu=[]
        largueur=len(dataset.donnees_covid.liste[0])
        longueur = len(dataset.donnees_covid.liste)-1
        for i in range(largueur):
            if type(dataset.donnees_covid.liste[1][i])==float:
                var=0
                moy=self.moyenne(dataset)[largueur-1-i][1]
        
                for donnees in dataset.donnees_covid.liste[1:]:
                    var= var+(float(donnees[i])-moy)**2
                resu.append(['{}'.format(dataset.donnees_covid.liste[0][i]),var/longueur])
        return resu

    def ecart_type(self,dataset):
        resu=[]
        var=self.variance(dataset)
        for ligne in var:
            resu.append([ligne[0],ligne[1]**(0.5)])

        return resu


    

