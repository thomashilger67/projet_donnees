from Transformation.transformation import Transformation
from Donnees.dataset import Dataset 
from Donnees.donnees_covid import Covid
from Donnees.donnees_vacances import Vacance

class Fenetrage(Transformation):
        
    ''' Classe héritant de la classe Transformation. Elle permet de selectionner les donneés d'un dataset 
    sur une plage temporelle finis.
    
    Parameters
    ----------

    donnees : str
        type de donnée : covid ou vacance
    
    var_selection : str
        éventuelle variable étudiée lors de la tansformation

    date_debut : str
        Date débutant la période étudiée.
    
    date_fin : str
        Date finissant la période étudiée.
    
    Attributs 
    ---------

    donnees : str
        type de donnée : covid ou vacance
    
    var_selection : str
        éventuelle variable étudiée lors de la tansformation

    date_debut : str
        Date débutant la période étudiée.
    
    date_fin : str
        Date finissant la période étudiée.
    
    Example 
    -------
     >>> d=Covid('./Donnees/Donnees_Covid/covid-hospit-incid-reg-2021-03-03-17h20.csv')
     >>> b=Vacance('./Donnees/vacances.json')
     >>> data= Dataset(d,b)
     >>> print(Fenetrage('NumReg', 'covid', '2020-03-019', '2020-03-20').application(Dataset(d)).donnees_covid)
    
    '''
    def __init__(self,var_selection,donnees,date_debut,date_fin):
        super().__init__(var_selection,donnees)
        self.date_fin = date_fin
        self.date_debut = date_debut
    
    def application_Covid(self, dataset):
        list_covid = dataset.donnees_covid.liste
        list_date = []
        indice_date=list_covid[0].index('jour')
        for x in list_covid[1:] :
            list_date.append([int(y) for y in x[indice_date].split('-')])
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
        new_jeu_covid =[list_covid[0]]
        for i in range(len(list_covid)-1):
            date = list_date[i]
            if convient(date):
                new_jeu_covid.append(list_covid[i+1])
        return Dataset(Covid(None,new_jeu_covid),dataset.donnees_vacances)

    def application_Vacance(self, dataset):
        vacances = dataset.donnees_vacances.dictionnaire
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
        list_calendrier = []
        for i in range(len(vacances['Calendrier'])):
            if (vacances['Calendrier'][i]['Debut'] != None ) and (vacances['Calendrier'][i]['Fin'] != None) :
                vac_debut = [int(x) for x in vacances['Calendrier'][i]['Debut'].split('-')]
                vac_fin = [int(x) for x in vacances['Calendrier'][i]['Fin'].split('-')]
                if convient(vac_debut) and convient(vac_fin):
                    list_calendrier.append(vacances['Calendrier'][i])
        return Dataset(dataset.donnees_covid,Vacance(None,{'Calendrier': list_calendrier, 'Academie': vacances['Academie']}))

