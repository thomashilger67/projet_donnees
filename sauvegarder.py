from dataset import Dataset
import csv

class Sauvegarder:

    def __init__(self,donnees_a_sauvgarder):
        self.donnees_a_sauvgarder=donnees_a_sauvgarder

    def SauvegarderCSV(self,nom_du_fichier):
        
       
       with open(nom_du_fichier, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC,delimiter=';')
        writer.writerows(self.donnees_a_sauvgarder.donnees_covid.liste)
        

