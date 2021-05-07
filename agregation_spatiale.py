from dataset import Dataset
from selection_variable import Selection_Var
from donnees_vacances import Vacance
from donnees_covid import Covid





class Agregation_Spatiale:

    

    def __init__(self,var_selection=None,region=None):
        self.var_selection=var_selection
        self.region=region
        
    def reg(self):

        vac=Vacance('./Donnees/vacances.json')
        liste_academie=vac.dictionnaire['Academie']
        dep_region=[]
        for elt in liste_academie:
            dep_region.append({'dep':elt['Code_Dpt'],'region':elt['Region']})
        return(dep_region)

    def application_nationale(self,dataset): #problème
        new_dataset=Selection_Var(self.var_selection,'covid').application_Covid(dataset)
        somme=0
        for i in range(1,len(new_dataset)):
            somme+=new_dataset[i]
        return(Dataset(['nationale',{self.var_selection: somme}])) #à revoir le return et la présentation???

    def application_regionale(self,dataset):
        dep_region=self.reg()
        data_dep=Selection_Var('dep','covid').application_Covid(dataset)










