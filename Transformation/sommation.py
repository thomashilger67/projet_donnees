from Transformation.transformation import Transformation
from Donnees.donnees_covid import Covid
from Donnees.dataset import Dataset

class Sommation(Transformation):

    def __init__(self,var_selection,donnees,granularite):
        super().__init__(var_selection, donnees)
        self.granularite=granularite


    def application_Covid(self, dataset):
        new_list=dataset.donnees_covid.liste[0:102]
        indice=new_list[0].index(self.var_selection)
        if self.granularite=="departement":
            for i in range(1,len(new_list)):
                for j in range(102,len(dataset.donnees_covid.liste)):
                    if dataset.donnees_covid.liste[i][0]==dataset.donnees_covid.liste[j][0]:
                        new_list[i][indice]+=dataset.donnees_covid.liste[j][indice]
    
        return Dataset(Covid(None,new_list),dataset.donnees_vacances)
                            




    def application_Vacance(self, dataset):
        pass
        