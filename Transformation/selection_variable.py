from Donnees.dataset import Dataset
from Transformation.transformation import Transformation
from Donnees.donnees_covid import Covid 



#comprendre application dans la classe transfo : l'appliquer à un argument 

class Selection_Var(Transformation):
    ''' Classe héritant de la classe Transformation. Elle permet de selectionner une variable dans un Dataset.

     
     Parameters
     ----------

     donnees : str
         type de donnée : covid ou vacance
     
     var_selection : str
         éventuelle variable étudiée lors de la tansformation

     Attributs 
     ---------

     donnees : str
         type de donnée : covid ou vacance
     
     var_selection : str
         éventuelle variable étudiée lors de la tansformation

     Example 
     -------

     >>> d = Dataset(Covid('./Donnees/Donnees_Covid/covid-hospit-incid-reg-2021-03-03-17h20.csv'),Vacance('./Donnees/vacances.json'))
     >>> s = Selection_Var('incid_rea','covid')
     >>> print(s.application(d.donnees_covid))

     '''

    def __init__(self,var_selection,donnees): 
        super().__init__(var_selection,donnees)
              
    
    def application_Covid(self,dataset):
        new_list=[]
        covid=dataset.donnees_covid.liste
        indice=covid[0].index(self.var_selection)
        for elt in covid:
            new_list.append([elt[indice]])
        return(Dataset(Covid(None,new_list),dataset.donnees_vacances))

    def application_Vacance(self,dataset):
        vacances=dataset.donnees_vacances
        new_list=[]
        if self.var_selection in vacances['Calendrier'][0]:
            for elt in vacances['Calendrier']:
                new_list.append(elt[self.var_selection])
        else:
            for elt in vacances['Academie']:
                new_list.append(elt[self.var_selection])
        new_list.insert(0,self.var_selection)
        return(Dataset(dataset.donnees_covid,new_list))
                    
        

        