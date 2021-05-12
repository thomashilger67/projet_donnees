from Transformation.transformation import Transformation
from Donnees.donnees_covid import Covid
from Donnees.donnees_vacances import Vacance
from Donnees.dataset import Dataset 

class Moyenne_glissante(Transformation):
    '''Classe héritant de la classe Transformation. Elle permet de la moyenne glissante d'une variable dans un Dataset.

     
     Parameters
     ----------

     donnees : str
         type de donnée : covid ou vacance
     
     var_selection : str
         éventuelle variable étudiée lors de la tansformation

     time : int
         Plage de la moyenne glissante
     
     Attributs 
     ---------

     donnees : str
         type de donnée : covid ou vacance
     
     var_selection : str
         éventuelle variable étudiée lors de la tansformation

     time : int
         Plage de la moyenne glissante
     
     Example 
     -------
    '''
    
    def __init__(self, var_selection, donnees, time):
        super().__init__(var_selection, donnees)
        self.time = time
    
    def application_Covid(self, dataset):
        list_covid = dataset.donnees_covid.liste
        indice_var= list_covid[0].index(self.var_selection)
        list_moyenne =[[self.var_selection]]
        for i in range(self.time, len(list_covid)):
            moyenne = 0
            for x in list_covid[i-self.time +1: i]:
                moyenne += x[indice_var]
            moyenne /= self.time 
            list_moyenne.append([moyenne])
        return Dataset(Covid(None,list_moyenne),dataset.donnees_vacances)
    

    def application_Vacance(self, dataset):
        return( "Il n'y a pas de moyenne glissante pour les vacances")
