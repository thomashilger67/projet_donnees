from estimation import Estimation
from dataset import Dataset

class EstimationDescriptive(Estimation):
    def __init__(self):
        pass
        

    def moyenne(self,dataset):
        sum=0
        largeur = len(dataset.donnees_covid.liste[0]) -1
        longueur = len(dataset.donnees_covid.liste)
        for donnees in dataset.donnees_covid.liste[1:]:
            sum=sum + float(donnees[largeur])
        
        return sum/longueur

    def variance(self,dataset):
        var=0
        moy=self.moyenne(dataset)
        largeur = len(dataset.donnees_covid.liste[0]) -1
        longueur = len(dataset.donnees_covid.liste)
        for donnees in dataset.donnees_covid.liste[1:]:
            var= var+(float(donnees[largeur])-moy)**2
        return var/longueur

    def ecart_type(self,dataset):
        var=self.variance(dataset)
        return var**(0.5)


    

