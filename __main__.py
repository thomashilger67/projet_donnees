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


a=Covid('./Donnees/Donnees_Covid/donnees-hospitalieres-covid19-2021-03-03-17h03.csv')
b=Vacance('./Donnees/vacances.json')
c=Covid('./Donnees/Donnees_Covid/donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv')
d=Covid('/Users/thomashilger/Desktop/projet_donnees/Donnees/Donnees_Covid/covid-hospit-incid-reg-2021-03-03-17h20.csv')

d=Covid('/Users/thomashilger/Desktop/projet_donnees/Donnees/Donnees_Covid/covid-hospit-incid-reg-2021-03-03-17h20.csv')
data=Dataset(d,b)

print(EstimationDescriptive().ecart_type(data).donnees_covid.liste)
#Sauvegarder(Normalisation('numReg','covid').application(data)).SauvegarderCSV('normal')
#print(Fenetrage('NumReg', 'covid', '2020-03-019', '2020-03-20').application(Dataset(d)).donnees_covid)


#Sauvegarder(a.liste).SauvegarderCSV('test',sep=',')
#Jointure('incid_hosp','vacance','Zone').application(data)

#print(EstimationDescriptive().ecart_type(data))


#data2=Dataset(c.liste)

#print(Jointure('hosp','covid',"incid_hosp",data2).application(data))


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