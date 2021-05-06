from dataset import Dataset

class Selection_Var:

    def __init__(self,selection):
        self.selection=selection
    
    def application(self,dataset):
        covid=dataset.donnees_covid
        vacance=dataset.donnees_vacances
        new_list=[]
        for var in self.selection :
            if var  in covid[0]:
                indice=covid[0].index(var)
                for i in len(covid):
                    new_list.append(covid[i][indice])
                    #prendre la position dans la liste puis extraire toutes les valeurs à cett position
            else : #c'est dans vacances
        

        #sélection des varibles ->>> on peut sélectionner la réanimation à tel jour?