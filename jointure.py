from dataset import Dataset
from transformation import Transformation
from selection_variable import Selection_Var

class Jointure(Transformation):
    
    def __init__(self,var_selection,donnees,var_jointure,dataset2):
        super().__init__(var_selection,donnees)
        self.var_jointure=var_jointure
        self.dataset2=dataset2
    
    def application_Covid(self,dataset):
        donnees_covid=dataset.donnees_covid
        donnees_covid2=self.dataset2.donnees_covid
        
        if self.var_selection in donnees_covid[0]:
            new_dataset=Selection_Var(self.var_selection,'covid').application_Covid(dataset)
        elif self.var_jointure in donnees_covid[0]:
            new_dataset=Selection_Var(self.var_jointure,'covid').application_Covid(dataset)

         #Joindre sur quoi? attention à sexe et numReg nomReg... compliqué

        if self.var_selection in donnees_covid2[0]:
            dataset_temp=Selection_Var(self.var_selection,'covid').application_Covid(self.dataset2)
        elif self.var_jointure in donnees_covid2[0]:
            dataset_temp=Selection_Var(self.var_jointure,'covid').application_Covid(self.dataset2)
        
        for i in range(len(new_dataset.donnees_covid)):
            new_dataset.donnees_covid[i].append(dataset_temp.donnees_covid[i][0])
        
        return(new_dataset)

    def application_Vacance(self,dataset):
        pass





