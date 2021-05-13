from Donnees.donnees_covid import Covid
from Donnees.donnees_vacances import Vacance
from Donnees.dataset import Dataset 

def fusion(dataset1,dataset2):
    '''fonction qui prend 2 datasets de même longueur et largeur en argument et les juxtapose dans un nouveau dataset

    Paramters
    ----------
    dataset1 : Dataset
    dataset2 : Dataset

    Returns
    ----------
    Dataset
        fusion des deux datasets
    
    '''
    for i in range(len(dataset2.donnees_covid.liste[0])):
        for j in range(len(dataset1.donnees_covid.liste)):
            dataset1.donnees_covid.liste[j].append(dataset2.donnees_covid.liste[j][i])
    return dataset1