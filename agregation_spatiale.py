from dataset import Dataset
from selection_variable import Selection_Var
from donnees_vacances import Vacance
from donnees_covid import Covid


class Agregation_Spatiale:

    
    def __init__(self,var_selection,region=None):
        self.var_selection=var_selection
        self.region=region
        
    def reg(self):

        vac=Vacance('./Donnees/vacances.json')
        liste_academie=vac.dictionnaire['Academie']
        dep_region=[]
        for elt in liste_academie:
            dep_region.append({'dep':elt['Code_Dpt'],'region':elt['Region']})
        return(dep_region)

    def application_nationale(self,dataset): 
        new_dataset=Selection_Var(self.var_selection,'covid').application_Covid(dataset)
        somme=0
        if self.var_selection=="rad" or self.var_selection=="dc":
            indice_jour=dataset.donnees_covid[0].index("jour")
            date=dataset.donnees_covid[-1][indice_jour]
            pos=len(dataset.donnees_covid)-1
            if 'sexe' in dataset.donnees_covid[0]:
                    indice_sexe=dataset.donnees_covid[0].index("sexe")
            while dataset.donnees_covid[pos][indice_jour]==date:
                if dataset.donnees_covid[pos][indice_sexe]==float(0):
                    somme+=new_dataset[pos]
                pos-=1
        else:
            for i in range(1,len(new_dataset)):
                somme+=new_dataset[i]
        return(Dataset([['Nationale',self.var_selection],['France',somme]])) 

    def application_regionale(self,dataset):
        dep_region=self.reg()
        liste_dep=[]
        somme=0
        for i in range(len(dep_region)):
            if dep_region[i]["region"]==self.region:
                liste_dep.append(float(dep_region[i]["dep"]))
        
        indice_var=dataset.donnees_covid[0].index(self.var_selection)
        data_dep=Selection_Var('dep','covid').application_Covid(dataset)
      
        if self.var_selection=="rad" or self.var_selection=="dc":
            indice_jour=dataset.donnees_covid[0].index("jour")
            date=dataset.donnees_covid[-1][indice_jour]
            pos=len(dataset.donnees_covid)-1
            if 'sexe' in dataset.donnees_covid[0]:
                    indice_sexe=dataset.donnees_covid[0].index("sexe")
            while dataset.donnees_covid[pos][indice_jour]==date:
                if dataset.donnees_covid[pos][indice_sexe]==float(0) and data_dep[pos] in liste_dep:
                    somme+=dataset.donnees_covid[pos][indice_var]
                pos-=1
        else:
            for i in range(1,len(data_dep)):
                if data_dep[i] in liste_dep:
                    somme+=dataset.donnees_covid[i][indice_var]
        return(Dataset([["Region",self.var_selection],[self.region,somme]]))










