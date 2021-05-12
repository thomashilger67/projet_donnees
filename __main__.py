from Donnees.donnees_covid import Covid
from Donnees.donnees_vacances import Vacance
from Donnees.dataset import Dataset
from Transformation.fenetrage import Fenetrage
from Estimation.estimation_descriptive import EstimationDescriptive
from Estimation.estimation_multivariee import EstimationMultivariee
from Transformation.selection_variable import Selection_Var
from Transformation.agregation_spatiale import Agregation_Spatiale
from Transformation.jointure import Jointure
from Transformation.centrage import Centrage
from Transformation.normalisation import Normalisation
from Sauvegarder.sauvegarder import Sauvegarder
from Sauvegarder.carte.cartoplot import CartoPlot
from Transformation.fenetrage import Fenetrage
from Transformation.moyenne_glissante import Moyenne_glissante
from Transformation.sommation import Sommation


a=Covid('./Donnees/Donnees_Covid/donnees-hospitalieres-covid19-2021-03-03-17h03.csv')
b=Vacance('./Donnees/vacances.json')
c=Covid('./Donnees/Donnees_Covid/donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv')
d=Covid('/Users/thomashilger/Desktop/projet_donnees/Donnees/Donnees_Covid/covid-hospit-incid-reg-2021-03-03-17h20.csv')
data=Dataset(d)

#print(Moyenne_glissante('numReg', 'covid', 20).application(data).donnees_covid.liste)

#Sauvegarder(Normalisation('numReg','covid').application(data)).SauvegarderCSV('normal')
#print(Fenetrage('numReg', 'covid', '2020-03-019', '2020-03-20').application(Dataset(d)).donnees_covid)
#Jointure('incid_hosp','vacance','Zone').application(data)
#print(Jointure('hosp','covid',"incid_hosp",data2).application(data))
#Selection_Var('numReg','covid').application(data).donnees_covid
#data=(Selection_Var('jour','Covid').application(data))
#Agregation_Spatiale("incid_hosp",'Covid','Occitanie').application(data))  #chiffre eh dessous des offciciels ???
#print(Normalisation('numReg','covid').application(data).donnees_covid.liste)


########QUESTIONS###########################



##Question2
#Combien de nouvelles hospitalisations ont eu lieu ces 7 derniers jours dans chaque département ? 

donnees_brute=Covid('/Users/thomashilger/Desktop/projet_donnees/Donnees/Donnees_Covid/donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv')
#on le transforme en dataset
dataset=Dataset(donnees_brute)

#on va d'abord fenetrer sur les 7 derniers jours
dataset_fenetre=Fenetrage('incid_hosp','covid', '2021-02-25', '2021-03-03').application(dataset)

#on somme les nombres d'hospitalisations par département
dataset_somme=Sommation('incid_hosp','covid','departement').application(dataset_fenetre)

#on sélectionne la variavble qui nous interesse
data_final=Selection_Var('incid_hosp', 'covid').application(dataset_somme)

#on sauvegarde dans un fichier csv

Sauvegarder(data_final).SauvegarderCSV('question2')

##Question3
