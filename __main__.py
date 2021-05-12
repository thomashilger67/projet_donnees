from donnees_covid import Covid
from donnees_vacances import Vacance
from dataset import Dataset
from fenetrage import Fenetrage
from estimation_descriptive import EstimationDescriptive
from estimation_multivariee import EstimationMultivariee
from selection_variable import Selection_Var
from agregation_spatiale import Agregation_Spatiale
from jointure import Jointure
from centrage import Centrage
from normalisation import Normalisation
from sauvegarder import Sauvegarder
from carte.cartoplot import CartoPlot


a=Covid('./Donnees/Donnees_Covid/donnees-hospitalieres-covid19-2021-03-03-17h03.csv')
b=Vacance('./Donnees/vacances.json')
c=Covid('./Donnees/Donnees_Covid/donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv')

#d=Covid('/Users/thomashilger/Desktop/projet_donnees/Donnees/Donnees_Covid/covid-hospit-incid-reg-2021-03-03-17h20.csv')


#d=Covid('/Users/thomashilger/Desktop/projet_donnees/Donnees/Donnees_Covid/covid-hospit-incid-reg-2021-03-03-17h20.csv')
data=Dataset(a,b.dictionnaire)

print(a.liste[0].index("dc"))
#print(b.dictionnaire)

#Sauvegarder(data).SauvegarderCSV('sauvegarde')


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
#print(data.donnees_covid.liste[0])
#print(data2)

#print(Selection_Var('numReg','covid').application(data).donnees_covid)

#Sauvegarder(Selection_Var('numReg','covid').application(data)).SauvegarderCSV('selection.csv')
#Agregation_Spatiale("incid_hosp",'Covid','Occitanie').application(data))  #chiffre eh dessous des offciciels ???


#print(EstimationMultivariee().Kmeans(data,2,2))
#print(type(EstimationDescriptive().moyenne(data)))
#print(EstimationDescriptive().moyenne(data))

#Sauvegarder(EstimationDescriptive().moyenne(data)).SauvegarderCSV('moyenne',';')
#print(Normalisation('numReg','covid').application(data).donnees_covid.liste)
