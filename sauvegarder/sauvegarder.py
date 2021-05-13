from Donnees.dataset import Dataset
import csv
import json 

class Sauvegarder:

    def __init__(self,donnees_a_sauvgarder):
        self.donnees_a_sauvgarder=donnees_a_sauvgarder

    def SauvegarderCSV(self,nom_du_fichier):
    

        with open('{}.csv'.format(nom_du_fichier), 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC,delimiter=';')
            writer.writerows(self.donnees_a_sauvgarder.donnees_covid.liste)
        
        '''else : 
            with open('{}.csv'.format(nom_du_fichier), 'w', newline='') as file:
                writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC,delimiter=';')
                writer.writerows(self.donnees_a_sauvgarder.donnees_covid.liste)
            with open('{}_vacances.csv'.format(nom_du_fichier), 'w',newline='') as file :
                writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC,delimiter=';')
                for key,ligne in self.donnees_a_sauvgarder.donnees_vacances.dictionnaire.items():
                    for element in ligne:
                        writer.writerows(ligne)'''
