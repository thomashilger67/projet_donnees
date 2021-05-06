from dataset import Dataset
from selection_variable import Selection_Var

class Agregation_Spatiale:
    def __init__(self,selection):
        self.selection=selection
    
    def application_nationale(self,dataset):
        new_dataset=Selection_Var.application(dataset)
        somme=0
        for i in range(1,len(new_dataset)):
            somme+=new_dataset[i]
        return(Dataset(['nationale',var])) #???

    def application_regionale(self,dataset)