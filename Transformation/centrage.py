from Transformation.transformation import Transformation
from Estimation.estimation_descriptive import EstimationDescriptive
from Donnees.donnees_covid import Covid
from Donnees.dataset import Dataset

class Centrage(Transformation):
    ''' Classe héritant de la classe Transformation. Elle permet de centrer une variable dans un Dataset.

     
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
    '''
    def __init__(self,var_selection,donnees):
        super().__init__(var_selection,donnees)

    def application_Covid(self, dataset):
        moyenne=0
        moyenne_dataset=EstimationDescriptive().moyenne(dataset)
        for ligne in moyenne_dataset:
            if self.var_selection==ligne[0]:
                moyenne=ligne[1]

        dataset_sortie=dataset
        for ligne in dataset_sortie.donnees_covid.liste[1:]:
            ligne[0]= ligne[0] - moyenne 
        return dataset_sortie

    def application_Vacance(self,dataset):
        pass