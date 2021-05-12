from Donnees.dataset import Dataset
from Transformation.transformation import Transformation
from Donnees.donnees_covid import Covid
from Transformation.centrage import Centrage
from Estimation.estimation_descriptive import EstimationDescriptive

class Normalisation(Transformation):
    ''' Classe héritant de la classe Transformation. Elle permet de centrer et réduire une variable dans un Dataset.

     
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
     >>> d=Covid('/Users/thomashilger/Desktop/projet_donnees/Donnees/Donnees_Covid/covid-hospit-incid-reg-2021-03-03-17h20.csv')
     >>> b=Vacance('./Donnees/vacances.json')
     >>> data= Dataset(d,b)
     >>> print(Normalisation('numReg','covid').application(data).donnees_covid.liste)
     '''

    def __init__(self,var_selection,donnees):
        super().__init__(var_selection,donnees)

    def application_Covid(self, dataset):
        ecart_type=EstimationDescriptive().ecart_type(dataset).donnees_covid.liste
        sd=0
        indice=dataset.donnees_covid.liste[0].index(self.var_selection)
        for ligne in ecart_type:
            if self.var_selection==ligne[0]:
                sd=ligne[1]

        dataset_sortie_centree=Centrage(self.var_selection,self.donnees).application(dataset)
        for ligne in dataset_sortie_centree.donnees_covid.liste[1:]:
            ligne[indice]=ligne[indice]/sd
        return dataset_sortie_centree

    def application_Vacance(self, dataset):
        pass
