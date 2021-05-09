from donnees_covid import Covid
from donnees_vacances import Vacance
from dataset import Dataset
from fenetrage import Fenetrage
from estimation_descriptive import EstimationDescriptive
from estimation_multivariee import EstimationMultivariee
from selection_variable import Selection_Var
from agregation_spatiale import Agregation_Spatiale
from jointure import Jointure

a=Covid('./Donnees/Donnees_Covid/donnees-hospitalieres-covid19-2021-03-03-17h03.csv')
b=Vacance('./Donnees/vacances.json')
c=Covid('./Donnees/Donnees_Covid/donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv')

data=Dataset(a.liste)

data2=Dataset(c.liste)

#print(Jointure('hosp','covid',"incid_hosp",data2).application(data))

print(Selection_Var("hosp",'covid').application(data))
#print(Agregation_Spatiale("dc",'Covid','Occitanie').application(data))  #chiffre eh dessous des offciciels ???

estimation=EstimationMultivariee()
#print(estimation.Kmeans(data,2,2))

#print(estimation.ecart_type(data))