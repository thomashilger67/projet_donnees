from dataset import Dataset
from transformation import Transformation


#comprendre application dans la classe transfo : l'appliquer à un argument 

class Selection_Var:

    def __init__(self,selection,select_fichier): #select_fichier
        self.selection=selection
        self.select_fichier=select_fichier
    
    def application_Covid(self,dataset):
        new_list=[]
        covid=dataset.donnees_covid
        indice=covid[0].index(self.selection)
        for elt in covid:
            new_list.append(elt[indice])

        return(new_list)

    def application_Vacance(self,dataset):
        vacances=dataset.donnees_vacances
        new_list=[]
        if self.selection in vacances['Calendrier'][0]:
            for elt in vacances['Calendrier']:
                new_list.append(elt[self.selection])
        else:
            for elt in vacances['Academie']:
                new_list.append(elt[self.selection])
        return(new_list)
                    
        

        