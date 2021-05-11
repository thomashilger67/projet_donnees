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
<<<<<<< HEAD
#d=Covid('/Users/thomashilger/Desktop/projet_donnees/Donnees/Donnees_Covid/covid-hospit-incid-reg-2021-03-03-17h20.csv')
data=Dataset(c)
data.donnees_covid.liste[1]
#print(data)
=======
d=Covid('/Users/thomashilger/Desktop/projet_donnees/Donnees/Donnees_Covid/covid-hospit-incid-reg-2021-03-03-17h20.csv')
data=Dataset(d)

>>>>>>> 0c3a1d44d2ec1db25dfc8e5f9dc297207f384039
#Sauvegarder(a.liste).SauvegarderCSV('test',sep=',')
#Jointure('incid_hosp','vacance','Zone').application(data)

#print(EstimationDescriptive().ecart_type(data))


#data2=Dataset(c.liste)

#print(Jointure('hosp','covid',"incid_hosp",data2).application(data))

<<<<<<< HEAD
data=(Selection_Var('jour','Covid').application(data))
print(data.donnees_covid.liste[0])
#print(data2)
=======
print(Selection_Var('numReg','covid').application(data).donnees_covid)
#print(data)
>>>>>>> 0c3a1d44d2ec1db25dfc8e5f9dc297207f384039
#Sauvegarder(Selection_Var('numReg','covid').application(data)).SauvegarderCSV('selection.csv')
(Agregation_Spatiale("incid_hosp",'Covid','Occitanie').application(data))  #chiffre eh dessous des offciciels ???


#print(EstimationMultivariee().Kmeans(data,2,2))
#print(type(EstimationDescriptive().moyenne(data)))
#print(EstimationDescriptive().moyenne(data))

#Sauvegarder(EstimationDescriptive().moyenne(data)).SauvegarderCSV('moyenne',';')
#print(Normalisation('numReg','covid').application(data).donnees_covid.liste)

############################CARTE##########################
cp=CartoPlot(())
d = {}
for i in range(1, 101):
   d[str(i)] = i


fig = cp.plot_dep_map(data=d, x_lim=(-6, 10), y_lim=(41, 52))
fig.show()
fig.savefig('departements.test.jpg')