from Données.donnees_Covid import Covid
from Données.donnees_Vacances import Vacance
from Données.dataset import Dataset

a = Covid('./Données/Données Covid/covid-hospit-incid-reg-2021-03-03-17h20.csv')
#print(a.dictionnaire)


b=Vacance('./Données/vacances.json')

#print(b.dictionnaire)

#d={"id":0,"Description":"Vacances de Noël","DateDebut":"lundi 21 décembre 2009","DateFin":"lundi 04 janvier 2010","Zone":"Corse","annee_scolaire":"2009-2010","Debut":"2009-12-21","Fin":"2010-01-04"}
#b.dictionnaire['Calendrier'].append(d)
#print(b.dictionnaire['Calendrier'])


