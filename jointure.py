from dataset import Dataset
from transformation import Transformation
from selection_variable import Selection_Var

class Jointure(Transformation):
    
    def __init__(self,var_selection,donnees,var_jointure,dataset2=None):
        super().__init__(var_selection,donnees)
        self.var_jointure=var_jointure
        self.dataset2=dataset2
    
    def application_Covid(self,dataset):
        donnees_covid=dataset.donnees_covid
        donnees_covid2=self.dataset2.donnees_covid
        
        indice_jour=donnees_covid[0].index("jour")
        indice_jour2=donnees_covid2[0].index("jour")
        new_dataset=Dataset([],dataset.donnees_vacances)
        indice_sexe=None
        
        if "reg" in donnees_covid[0]:
            indice_spatial=donnees_covid[0].index("reg")
        elif "dep" in donnees_covid[0]:
            indice_spatial=donnees_covid[0].index("dep")
        elif "numReg" in donnees_covid[0]:
            indice_spatial=donnees_covid[0].index("Numreg")
        
        if 'sexe' in donnees_covid[0]:
            indice_sexe=donnees_covid[0].index("sexe")
               
        if self.var_selection in donnees_covid[0]:
            indice1=donnees_covid[0].index(self.var_selection)
        elif self.var_jointure in donnees_covid[0]:
            indice1=donnees_covid[0].index(self.var_jointure)
        if self.var_selection in donnees_covid2[0]:
            indice2=donnees_covid2[0].index(self.var_selection)
        elif self.var_jointure in donnees_covid2[0]:
            indice2=donnees_covid2[0].index(self.var_jointure)

        new_dataset.donnees_covid.append([donnees_covid[0][indice_spatial],donnees_covid2[0][indice_jour2],donnees_covid[0][indice1],donnees_covid2[0][indice2]])
        pos=1
        i=1
        if len(donnees_covid)>=len(donnees_covid2): #il y a plus de jours dans donnees_covid
            
            if indice_sexe==None : 
                while i<len(donnees_covid) and pos<(len(donnees_covid2)) : 
                    if donnees_covid[i][indice_jour]==donnees_covid2[pos][indice_jour2]:
                        new_dataset.ajout_donnees_covid([donnees_covid[i][indice_spatial],donnees_covid2[pos][indice_jour2],donnees_covid[i][indice1],donnees_covid2[pos][indice2]])
                        i+=1
                        pos+=1
                    else:
                        i+=1
            else: 
                while i<len(donnees_covid) and pos<(len(donnees_covid2)) :
                    if donnees_covid[i][indice_jour]==donnees_covid2[pos][indice_jour2]:
                        new_dataset.ajout_donnees_covid([donnees_covid[i][indice_spatial],donnees_covid2[pos][indice_jour2],donnees_covid[i][indice1],donnees_covid2[pos][indice2]])
                        i+=3
                        pos+=1   
                    else:
                        i+=3

        else:
           
            if indice_sexe==None:
                while i<len(donnees_covid2) and pos<(len(donnees_covid2)) : 
                    if donnees_covid2[i][indice_jour2]==donnees_covid[pos][indice_jour]:
                        new_dataset.ajout_donnees_covid([donnees_covid[pos][indice_spatial],donnees_covid[pos][indice_jour2],donnees_covid[pos][indice1],donnees_covid2[i][indice2]])
                        i+=1
                        pos+=1
                    else:
                        i+=1
            else: 
                while i<len(donnees_covid) and pos<(len(donnees_covid2)) : 
                    if donnees_covid2[i][indice_jour2]==donnees_covid[pos][indice_jour] :
                      
                        new_dataset.ajout_donnees_covid([donnees_covid[pos][indice_spatial],donnees_covid[pos][indice_jour2],donnees_covid[pos][indice1],donnees_covid2[i][indice2]])
                        i+=3
                        pos+=1
                    else:
                        i+=3
               
        return(new_dataset)

    def application_Vacance(self,dataset):
        donnees_covid=dataset.donnees_covid
        donnees_vacance=dataset.donnees_vacances
        indice_dep=donnees_covid[0].index("dep")
        indice_selection=donnees_covid[0].index(self.var_selection)
        new_dataset=Dataset([],dataset.donnees_vacances)
        endroit=None
        if self.var_jointure in donnees_vacance['Calendrier'][0]:
            endroit='Calendrier'
        elif self.var_jointure in donnees_vacance['Academie'][0]:
            endroit='Academie'
        else:
            print("La variable recherchée n'est pas présente. Revoyez l'écriture ou les données")

        for liste in donnees_covid :
            pos=1
            while donnees_vacance['Academie'][pos]["Code_Dpt"]!=liste[indice_dep]:
                pos+=1
            new_dataset.ajout_donnees_covid([liste[indice_dep],donnees_vacance['Academie'][pos]["Zone"],liste[indice_selection]])





        





