from abc import ABC, abstractmethod

class Transformation(ABC):

    
    def __init__(self,var_selection,donnees):
        self.var_selection=var_selection
        self.donnees=donnees

    @abstractmethod
    def application_Covid(self,dataset):
        pass
    
    @abstractmethod
    def application_Vacance(self,dataset):
        pass

    def application(self,dataset):
        return(self.application_Covid(dataset) if self.donnees.lower()=='covid' else self.application_Vacance(dataset) )
        
    #def __str__(self):
       # return "Les résultats sont les suivants : {}".format(self.application(dataset))

    #nefonctionne pas je ne sais pas comment faire pour appeler dataset sans le mettre en données_init