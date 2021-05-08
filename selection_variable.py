from dataset import Dataset
from transformation import Transformation


#comprendre application dans la classe transfo : l'appliquer à un argument 

class Selection_Var(Transformation):

    def __init__(self,var_selection,donnees): 
        super().__init__(var_selection,donnees)
      
    
    def application_Covid(self,dataset):
        new_list=[]
        covid=dataset.donnees_covid
        indice=covid[0].index(self.var_selection)
        for elt in covid:
            new_list.append(elt[indice])
        return(new_list)

    def application_Vacance(self,dataset):
        vacances=dataset.donnees_vacances
        new_list=[]
        if self.var_selection in vacances['Calendrier'][0]:
            for elt in vacances['Calendrier']:
                new_list.append(elt[self.var_selection])
        else:
            for elt in vacances['Academie']:
                new_list.append(elt[self.var_selection])
        return(new_list)
                    
        

        