from donnees_covid import Covid
from donnees_vacances import Vacance
from dataset import Dataset
from fenetrage import Fenetrage
from estimation_descriptive import EstimationDescriptive
from estimation_multivariee import EstimationMultivariee
from selection_variable import Selection_Var
from agregation_spatiale import Agregation_Spatiale

a = Covid('./Donnees/Donnees_Covid/covid-hospit-incid-reg-2021-03-03-17h20.csv')
b=Vacance('./Donnees/vacances.json')


#print(a.dictionnaire)

data=Dataset(a.liste,b.dictionnaire)





print((Agregation_Spatiale("incid_rea").application_regionale(data)))  #problème


estimation=EstimationMultivariee()
#print(estimation.Kmeans(data,2,2))

#print(estimation.ecart_type(data))