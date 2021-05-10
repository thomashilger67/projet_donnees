from transformation import Transformation
from estimation_descriptive import EstimationDescriptive
from donnees_covid import Covid
from dataset import Dataset

class Centrage(Transformation):

    def __init__(self,var_selection,donnees):
        super().__init__(var_selection,donnees)

    def application_Covid(self, dataset):
        moyenne=EstimationDescriptive().moyenne(dataset)
        dataset_sortie=dataset
        for ligne in dataset_sortie.donnees_covid.liste[1:]:
            ligne[0]= ligne[0] - moyenne 
        return dataset_sortie

    def application_Vacance(self,dataset):
        pass