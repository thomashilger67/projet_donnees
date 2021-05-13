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

def selection_sexe(dataset,sexe):
    ''' selectionne les lignes d'un dataset en fonction du sexe renseigné 
    0=hommes et femmes
    1= homme
    2= femme

    Parameters
    -----------
    dataset : Dataset

    sexe : str

    Returns 
    ----------
    Dataset
    '''
    
    new_list=[dataset.donnees_covid.liste[0]]

    indice_sexe=dataset.donnees_covid.liste[0].index('sexe')
    for ligne in dataset.donnees_covid.liste[1:]:
        if ligne[indice_sexe]==float(sexe):
            new_list.append(ligne)
        else: 
            pass
    
    return Dataset(Covid(None,new_list),dataset.donnees_vacances)