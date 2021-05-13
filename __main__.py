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
from fonctions import selection_sexe



########QUESTIONS###########################

##Question1
#Quel est le nombre total d'hospitalisation dues au Covid-19 ? 
'''
donnees_brute=Covid('./Donnees/Donnees_Covid/donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv')
dataset=Dataset(donnees_brute)

#On fait une agregation à l'echelle nationale
dataset_agrege=Agregation_Spatiale('incid_hosp', 'covid', 'region').application(dataset)

#on somme toutes les lignes 
dataset_somme=Sommation('incid_hosp', 'covid', 'nationale').application(dataset_agrege)

#on sauvegarde
Sauvegarder(dataset_somme).SauvegarderCSV('somme_nationale')
'''



##Question2
#Combien de nouvelles hospitalisations ont eu lieu ces 7 derniers jours dans chaque département ? 
'''
donnees_brute=Covid('./Donnees/Donnees_Covid/donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv')

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
donnees_brute=Covid('./Donnees/Donnees_Covid/donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv')
dataset=Dataset(donnees_brute)

#on crée un premier dataset contenant la moyenne de la semaine dernière
dataset_semaine_actuelle=EstimationDescriptive().moyenne(Selection_Var('incid_hosp', 'covid').application(Fenetrage('incid_hosp', 'covid', '2021-02-25', '2021-03-03').application(dataset)))


#on crée un deuxième dataset contenant la moyenne de la semaine actuelle 
dataset_semaine_precedente=EstimationDescriptive().moyenne(Selection_Var('incid_hosp', 'covid').application(Fenetrage('incid_hosp', 'covid', '2021-02-18', '2021-02-24').application(dataset)))

#on sauvegarde les deux datasets dans deux fichiers csv 
Sauvegarder(dataset_semaine_precedente).SauvegarderCSV('semaine_prec')
Sauvegarder(dataset_semaine_actuelle).SauvegarderCSV('semaine_act')
'''

##Question4
#Quel est le résultat de k-means avec k = 3 sur les données des 
# départements du mois de Janvier 2021, lissées avec une moyenne glissante de 7 jours ? 
'''
#Pour répondre à cette question notre Kmeans ne fonctionne qu'avec deux colonnes 

#On importe les données
donnees_hospitaliers=Dataset(Covid('/Users/thomashilger/Desktop/projet_donnees/Donnees/Donnees_Covid/donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv'))


#On fait un fenêtrage sur le mois de janvier
dataset=Fenetrage('incid_hosp', 'covid', '2021-01-01', '2021-01-31').application(donnees_hospitaliers)

#On crée deux dataset avec les moyennes glissantes pour les variables 'incid_hosp' et 'incid_rea'
dataset_gliss_1=Moyenne_glissante('incid_hosp', 'covid', 7).application(dataset)
dataset_gliss_2=Moyenne_glissante('incid_rea', 'covid', 7).application(dataset)

#on fusionne nos deux datasets pour en obtenir un nouveau 
dataset_fusion=fusion(dataset_gliss_1,dataset_gliss_2)

#on effectue le Kmeans
print(EstimationMultivariee().Kmeans(dataset_fusion, 3, 3))
'''

##Question5
#afficher sur une carte de France à l'echelle départmentale le nombre de personne de retour à domicile le 10 septembre 2020
'''
#on importe les donnees
donnees_brute=Dataset(Covid('./Donnees/Donnees_Covid/donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv'))

#on selectionne les données du 10/09/2020
dataset=Fenetrage('incid_rad', 'covid', '2020-09-10', '2020-09-10').application(donnees_brute)

#on adapte nos données pour la carte
donnees_carte=CartoPlot().nettoyage_donnee(dataset, 'departement', 'incid_rad')

#on affiche la carte
fig = CartoPlot().plot_dep_map(data=donnees_carte, x_lim=(-6, 10), y_lim=(41, 52))
fig.show()
fig.savefig('departements.test.jpg')
'''

##Question6
#Quel est le nombre de décès de femme  par région au mois le 31 décembre 2020

'''
#on importe les données 
donnees_brute=Dataset(Covid('./Donnees/Donnees_Covid/donnees-hospitalieres-covid19-2021-03-03-17h03.csv'))

#on agrège à l'echelle régionale 
donnees_agrege=Agregation_Spatiale('dc', 'covid', 'region').application(donnees_brute)

#on sélectionne la date du 31 décembre 2020
donnees_fenetre=Fenetrage('dc', 'covid', '2020-12-31', '2020-12-31').application(donnees_agrege)

#on sélectionne les lignes correspondants aux femmes
donnees_sexe=selection_sexe(donnees_fenetre, '2')

#on sauvegarde dans un fichier csv 
Sauvegarder(donnees_sexe).SauvegarderCSV('deces_femme_nouvel_an')
'''