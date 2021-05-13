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
from sauvegarder.sauvegarder import Sauvegarder
from sauvegarder.carte.cartoplot import CartoPlot
from Transformation.fenetrage import Fenetrage
from Transformation.moyenne_glissante import Moyenne_glissante
from Transformation.sommation import Sommation
from Transformation.agregation_spatiale import Agregation_Spatiale
from fonctions import fusion


a=Covid('./Donnees/Donnees_Covid/donnees-hospitalieres-covid19-2021-03-03-17h03.csv')
b=Vacance('./Donnees/vacances.json')
c=Covid('/Users/thomashilger/Desktop/projet_donnees/Donnees/Donnees_Covid/covid-hospit-incid-reg-2021-03-03-17h20.csv')
d=Covid('/Users/thomashilger/Desktop/projet_donnees/Donnees/Donnees_Covid/donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv')
data=Dataset(d,b)


########QUESTIONS###########################

##Question1
#Quel est le nombre total d'hosptilisation dues au Covid-19 ? 
'''
donnees_brute=Covid('/Users/thomashilger/Desktop/projet_donnees/Donnees/Donnees_Covid/donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv')
dataset=Dataset(donnees_brute)

#On fait une agregation à l'echelle nationale
dataset_agrege=Agregation_Spatiale('incid_hosp', 'covid', 'region').application(dataset)
dataset_somme=Sommation('incid_hosp', 'covid', 'nationale').application(dataset_agrege)
Sauvegarder(dataset_somme).SauvegarderCSV('somme_nationale')
'''



##Question2
#Combien de nouvelles hospitalisations ont eu lieu ces 7 derniers jours dans chaque département ? 
'''
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
'''


##Question3
#Comment évolue la moyenne des nouvelles hospitalisations
# journalières de cette semaine par rapport à celle de la semaine dernière ?
'''
donnees_brute=Covid('/Users/thomashilger/Desktop/projet_donnees/Donnees/Donnees_Covid/donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv')
dataset=Dataset(donnees_brute)
dataset_semaine_actuelle=EstimationDescriptive().moyenne(Selection_Var('incid_hosp', 'covid').application(Fenetrage('incid_hosp', 'covid', '2021-02-25', '2021-03-03').application(dataset)))



dataset_semaine_precedente=EstimationDescriptive().moyenne(Selection_Var('incid_hosp', 'covid').application(Fenetrage('incid_hosp', 'covid', '2021-02-18', '2021-02-24').application(dataset)))

Sauvegarder(dataset_semaine_precedente).SauvegarderCSV('semaine_prec')
Sauvegarder(dataset_semaine_actuelle).SauvegarderCSV('semaine_act')
'''

##Question4
#Quel est le résultat de k-means avec k = 3 sur les données des 
# départements du mois de Janvier 2021, lissées avec une moyenne glissante de 7 jours ? 

donnees_hospitaliers=Dataset(Covid('/Users/thomashilger/Desktop/projet_donnees/Donnees/Donnees_Covid/donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv'))
dataset=Fenetrage('incid_hosp', 'covid', '2021-01-01', '2021-01-31').application(donnees_hospitaliers)
dataset_gliss_1=Moyenne_glissante('incid_hosp', 'covid', 7).application(dataset)
dataset_gliss_2=Moyenne_glissante('incid_rea', 'covid', 7).application(dataset)

dataset_fusion=fusion(dataset_gliss_1,dataset_gliss_2)
Sauvegarder(dataset_fusion).SauvegarderCSV('fusion')