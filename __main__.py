from donnees_covid import Covid
from donnees_vacances import Vacance
from dataset import Dataset
from estimation_descriptive import EstimationDescriptive


a = Covid('./Donnees/Donnees_Covid/covid-hospit-incid-reg-2021-03-03-17h20.csv')
data=Dataset(a)

estimation=EstimationDescriptive()
print(estimation.ecart_type(data))
#b=Vacance('./Donnees/vacances.json')
#print(b.dictionnaire)
