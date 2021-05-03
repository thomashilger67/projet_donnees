from donnees_covid import Covid
from donnees_vacances import Vacance
from dataset import Dataset
<<<<<<< HEAD

a = Covid('./Donnees/Donnees_Covid/covid-hospit-incid-reg-2021-03-03-17h20.csv')
#print(a.dictionnaire)
print(a.dictionnaire[0])
=======
from estimation_descriptive import EstimationDescriptive
>>>>>>> e6b8f4b0f24fb027827509e9d187b6d0ab19654a


a = Covid('./Donnees/Donnees_Covid/covid-hospit-incid-reg-2021-03-03-17h20.csv')
data=Dataset(a)

<<<<<<< HEAD
print(a.dictionnaire[0][3],a.dictionnaire[1][3])

#d={"id":0,"Description":"Vacances de Noël","DateDebut":"lundi 21 décembre 2009","DateFin":"lundi 04 janvier 2010","Zone":"Corse","annee_scolaire":"2009-2010","Debut":"2009-12-21","Fin":"2010-01-04"}
#b.dictionnaire['Calendrier'].append(d)
#print(b.dictionnaire['Calendrier'])
d=Dataset(a.dictionnaire,b.dictionnaire)
#print(d)
#d.ajout_donnees_vacances('Academie',{'id': 276, 'Code_Dpt': '61', 'Dpt': '61 - Orne', 'Region': 'Normandie', 'Academie': 'de Caen', 'Zone': 'Zone B', 'NomAcademie': 'Caen', 'Departement': 'Orne'})

d.suppr_donnees_vacances('Calendrier',0)
#print(d.donnees_vacances['Calendrier'][0])


=======
estimation=EstimationDescriptive()
print(estimation.ecart_type(data))
#b=Vacance('./Donnees/vacances.json')
#print(b.dictionnaire)
>>>>>>> e6b8f4b0f24fb027827509e9d187b6d0ab19654a
