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


a=Covid('./Donnees/Donnees_Covid/donnees-hospitalieres-covid19-2021-03-03-17h03.csv')
b=Vacance('./Donnees/vacances.json')
c=Covid('./Donnees/Donnees_Covid/donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv')

<<<<<<< HEAD
#d=Covid('/Users/thomashilger/Desktop/projet_donnees/Donnees/Donnees_Covid/covid-hospit-incid-reg-2021-03-03-17h20.csv')


#d=Covid('/Users/thomashilger/Desktop/projet_donnees/Donnees/Donnees_Covid/covid-hospit-incid-reg-2021-03-03-17h20.csv')
data=Dataset(a,b.dictionnaire)

print(a.liste[0].index("dc"))
#print(b.dictionnaire)

#Sauvegarder(data).SauvegarderCSV('sauvegarde')
=======
d=Covid('/Users/thomashilger/Desktop/projet_donnees/Donnees/Donnees_Covid/covid-hospit-incid-reg-2021-03-03-17h20.csv')
data=Dataset(d)

print(Moyenne_glissante('numReg', 'covid', 20).application(data).donnees_covid.liste)

#Sauvegarder(Normalisation('numReg','covid').application(data)).SauvegarderCSV('normal')
#print(Fenetrage('numReg', 'covid', '2020-03-019', '2020-03-20').application(Dataset(d)).donnees_covid)
>>>>>>> f07064276af300b72b0d5984641fc461a17fe176


#Sauvegarder(a.liste).SauvegarderCSV('test',sep=',')


#print(EstimationDescriptive().ecart_type(data))


data2=Dataset(a)
#print(Covid(None,[["Academie"],['France']]))

#print((Jointure('incid_hosp','vacance',"Zone").application(data)))

print(Selection_Var('jour','Covid').application(data))

#print(data2)
#Sauvegarder(Selection_Var('numReg','covid').application(data)).SauvegarderCSV('selection.csv')
print((Agregation_Spatiale("dc",'Covid').application(data)))  #chiffre eh dessous des offciciels ???

#Selection_Var('numReg','covid').application(data).donnees_covid


#data=(Selection_Var('jour','Covid').application(data))

#print(Selection_Var('numReg','covid').application(data).donnees_covid)

#Sauvegarder(Selection_Var('numReg','covid').application(data)).SauvegarderCSV('selection.csv')
#Agregation_Spatiale("incid_hosp",'Covid','Occitanie').application(data))  #chiffre eh dessous des offciciels ???


#print(EstimationMultivariee().Kmeans(data,2,2))
#print(type(EstimationDescriptive().moyenne(data)))
#print(EstimationDescriptive().moyenne(data))

#Sauvegarder(EstimationDescriptive().moyenne(data)).SauvegarderCSV('moyenne',';')
#print(Normalisation('numReg','covid').application(data).donnees_covid.liste)