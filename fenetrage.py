from transformation import Transformation

class Fenetrage(Transformation):
    def __init__(self,date_debut,date_fin):
        self.date_fin = date_fin
        self.date_debut = date_debut
    
    def application(self,jeu_de_donnees):
        list_covid = jeu_de_donnees.__donnees_covid
        dic_vacances = jeu_de_donnees.__donnees_vacances 
        list_date = []
        for x in list_covid :
            list_date.append([int(y) for y in x[0].split('-')])
        debut = [int(x) for x in self.date_debut.split('-')]
        fin = [int(x) for x in self.date_fin.split('-')]
        def convient(date):
            if not(debut[0]<=date[0]<=fin[0]):
                return False
            elif ( debut[0] == date[0] and debut[1] > date[1] ) or (fin[0] == date[0] and fin[1] < date[1]):
                return False
            elif ( debut[0] == date[0] and debut[1] == date[1] and debut[2] > date[2]) or (fin[0] == date[0] and fin[1] == date[1] and fin[2] < date[2]):
                return False
            else :
                return True
        new_jeu_covid =[] 
        for i in range(len(list_covid)):
            date = list_date[i]
            if convient(date):
                new_jeu_covid.append(list_covid[i])
        return new_jeu_covid


