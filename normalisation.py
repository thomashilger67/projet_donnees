from dataset import Dataset
from transformation import Transformation
from donnees_covid import Covid
from centrage import Centrage
from estimation_descriptive import EstimationDescriptive

class Normalisation(Transformation):

    def __init__(self,var_selection,donnees):
        super().__init__(var_selection,donnees)

    def application_Covid(self, dataset):
        ecart_type=EstimationDescriptive().ecart_type(dataset)
        sd=0
        for ligne in ecart_type:
            if self.var_selection==ligne[0]:
                sd=ligne[1]

        dataset_sortie_centree=Centrage(self.var_selection,self.donnees).application(dataset)
        for ligne in dataset_sortie_centree.donnees_covid.liste[1:]:
            ligne[0]=ligne[0]/sd
        return dataset_sortie_centree

    def application_Vacance(self, dataset):
        pass
