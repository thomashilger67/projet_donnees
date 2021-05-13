from Transformation.transformation import Transformation
from Donnees.donnees_covid import Covid
from Donnees.dataset import Dataset

class Sommation(Transformation):
    ''' classe qui permet de sommer de manière temporelle les données  à l'echelle régionale ou départmentale

     
     Parameters
     ----------

     granularite : str 
            echelle soit 'region' soit 'departement'

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
     ------
     >>> donnees_brute=Covid('./Donnees/Donnees_Covid/donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv')
     >>> dataset=Dataset(donnees_brute)
     >>> dataset_agrege=Agregation_Spatiale('incid_hosp', 'covid', 'region').application(dataset)
     >>> dataset_somme=Sommation('incid_hosp', 'covid', 'nationale').application(dataset_agrege)
     >>> Sauvegarder(dataset_somme).SauvegarderCSV('somme_nationale')
     '''

    def __init__(self,var_selection,donnees,granularite):
        super().__init__(var_selection, donnees)
        self.granularite=granularite


    def application_Covid(self, dataset):
        
        if self.granularite=="departement":
            new_list=dataset.donnees_covid.liste[0:102]
            indice=new_list[0].index(self.var_selection)
            for i in range(1,len(new_list)):
                for j in range(102,len(dataset.donnees_covid.liste)):
                    if dataset.donnees_covid.liste[i][0]==dataset.donnees_covid.liste[j][0]:
                        new_list[i][indice]+=dataset.donnees_covid.liste[j][indice]
    
            return Dataset(Covid(None,new_list),dataset.donnees_vacances)
        
        elif self.granularite=='region':
            if 'nomReg' in dataset.donnees_covid.liste[0]:
                new_list=dataset.donnees_covid.liste[0:19]
                indice_reg=new_list[0].index('nomReg')
                
                indice=new_list[0].index(self.var_selection)
                for i in range(1,len(new_list)):
                    for j in range(19,len(dataset.donnees_covid.liste)):
                        if dataset.donnees_covid.liste[i][indice_reg]==dataset.donnees_covid.liste[j][indice_reg]:
                            new_list[i][indice]+=dataset.donnees_covid.liste[j][indice]

                return Dataset(Covid(None,new_list),dataset.donnees_vacances)
                
            if 'Region' in dataset.donnees_covid.liste[0]:
                new_list=[dataset.donnees_covid.liste[0]]
                indice_reg=new_list[0].index('Region')
                k=0
                indice=new_list[0].index(self.var_selection)
                for i in range(1,len(dataset.donnees_covid.liste)):
                    
                    if not dataset.donnees_covid.liste[i][indice_reg] in new_list[-1]:
                        new_list.append(dataset.donnees_covid.liste[i])
                        k=k+1
                        
                    
                    for j in range(i,len(dataset.donnees_covid.liste)):
                        if dataset.donnees_covid.liste[i][indice_reg]==dataset.donnees_covid.liste[j][indice_reg]:
                            new_list[k][indice]+=dataset.donnees_covid.liste[j][indice]

                return Dataset(Covid(None,new_list),dataset.donnees_vacances)



        elif self.granularite=='nationale':
            new_list=dataset.donnees_covid.liste[0:2]
            indice=new_list[0].index(self.var_selection)
            for j in range(1,len(dataset.donnees_covid.liste)):
                new_list[1][indice]+=dataset.donnees_covid.liste[j][indice]


            return Dataset(Covid(None,new_list),dataset.donnees_vacances)






    def application_Vacance(self, dataset):
        pass
        