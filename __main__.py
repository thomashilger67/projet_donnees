from donnees_covid import Covid
from donnees_vacances import Vacance
from dataset import Dataset
from fenetrage import Fenetrage

a = Covid('./Donnees/Donnees_Covid/covid-hospit-incid-reg-2021-03-03-17h20.csv')
# print(a.dictionnaire)


b=Vacance('./Donnees/vacances.json')

# print(b.dictionnaire)

#d={"id":0,"Description":"Vacances de Noël","DateDebut":"lundi 21 décembre 2009","DateFin":"lundi 04 janvier 2010","Zone":"Corse","annee_scolaire":"2009-2010","Debut":"2009-12-21","Fin":"2010-01-04"}
#b.dictionnaire['Calendrier'].append(d)
#print(b.dictionnaire['Calendrier'])
d =Dataset(a,b)
f = Fenetrage('2020-10-01', '2020-10-27')
print(f.application(d))

