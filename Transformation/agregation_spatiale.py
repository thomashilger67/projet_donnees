
from Donnees import donnees_vacances
from Donnees import donnees_covid
from Donnees.dataset import Dataset
from Transformation.selection_variable import Selection_Var
from Donnees.donnees_vacances import Vacance
from Donnees.donnees_covid import Covid
from Transformation.transformation import Transformation



class Agregation_Spatiale(Transformation):

    ''' Classe héritant de la classe Transformation. Elle permet de transformer la granularité départementale 
        en granularité nationale ou régionale
    
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

    granularité : str
        chaine de caractère indiquant l'échelle sur laquelle on effectue la granularité : 'nationale' ou 'region' 
    
        
    Example 
    -------
     >>> d=Covid('./Donnees/Donnees_Covid/donnees-hospitalieres-covid19-2021-03-03-17h03.csv')
     >>> b=Vacance('./Donnees/vacances.json')
     >>> data= Dataset(d,b)
     >>> print(Agregation('hosp', 'covid','region').application(data))
    
    '''
    
    def __init__(self,var_selection,donnees,granularite):
        super().__init__(var_selection,donnees)
        self.granularite=granularite
        
        
    def reg(self):
        ''' A partir de donnees_vacance, on extrait les départements en les associant à leurs régions.
            Puis, on crée une liste des région avec le nom de la région en première position suivie de ses départements.
            Enfin, on supprime les doublons.
        '''
        vac=Vacance('./Donnees/vacances.json')
        liste_academie=vac.dictionnaire['Academie']
        dep_region=[]
        liste_region=[]
        
        for elt in liste_academie:
            dep_region.append({'dep':elt['Code_Dpt'],'region':elt['Region']})

        for pos in range(len(dep_region)):
            region=dep_region[pos]['region']
            liste_region.append([region])
            for elt in dep_region:
                if elt['region']==region:
                    if elt['dep']=='2A' or elt['dep']=='2B':
                        liste_region[pos].append((elt['dep']))
                    else:
                        liste_region[pos].append(float(elt['dep']))
        
        liste_finale=[]
        for region in liste_region:
            if region not in liste_finale:
                liste_finale.append(region)
        return(liste_finale)            

    def sexe(self,dataset):
        ''' Fonction qui permet d'obtenir le premier indice d'apparition du sexe dans donnees_covid
        '''
        donnees_covid=dataset.donnees_covid.liste
        indice_sexe=donnees_covid[0].index("sexe")
        indice0=0
        while donnees_covid[indice0][indice_sexe]!=float(0):
            indice0+=1
            
        indice1=0
        while donnees_covid[indice1][indice_sexe]!=float(1):
            indice1+=1
            
        indice2=0
        while donnees_covid[indice2][indice_sexe]!=float(2):
            indice2+=1
        
        return(indice0,indice1,indice2)



    def application_nationale(self,dataset): 
        
        var_dataset=(Selection_Var(self.var_selection,'covid').application(dataset)).donnees_covid.liste
        donnees_covid=dataset.donnees_covid.liste
        somme=0
        indice_jour=donnees_covid[0].index("jour")

        if "sexe" in donnees_covid[0] :

            indice0,indice1,indice2=self.sexe(dataset)
        
            somme0=var_dataset[indice0][0]
            somme1=var_dataset[indice2][0]
            somme2=var_dataset[indice2][0]

            difference1=indice1-indice0
            difference2=indice2-indice0
            difference=indice2-indice0+1

            pos0=indice0+difference
            
            new_dataset=Dataset(Covid(None,[["Nationale",'jour','sexe',self.var_selection]]),dataset.donnees_vacances)
           
            while pos0<len(var_dataset)-difference :
                if donnees_covid[pos0][indice_jour]==donnees_covid[pos0-difference][indice_jour]:
                    somme0+=var_dataset[pos0][0]
                    somme1+=var_dataset[pos0+difference1][0]
                    somme2+=var_dataset[pos0+difference2][0]
                    pos0+=difference
                else:
                    new_dataset.ajout_donnees_covid(["France",donnees_covid[pos0][indice_jour],float(0),somme0])
                    new_dataset.ajout_donnees_covid(["France",donnees_covid[pos0+difference1][indice_jour],float(1),somme1])
                    new_dataset.ajout_donnees_covid(["France",donnees_covid[pos0+difference2][indice_jour],float(2),somme2])
                    somme0=var_dataset[pos0][0]
                    somme1=var_dataset[pos0+difference1][0]
                    somme2=var_dataset[pos0+difference2][0]
                    pos0+=difference
                
              
        else:
            new_dataset=Dataset(Covid(None,[["Nationale",'jour',self.var_selection]]),dataset.donnees_vacances)
            somme=var_dataset[1][0]
            i=2
            while i<len(var_dataset):
                if donnees_covid[i][indice_jour]==donnees_covid[i-1][indice_jour]:
                    somme+=var_dataset[i][0]
                    i+=1
                else:
                    new_dataset.ajout_donnees_covid(["France",donnees_covid[i][indice_jour],somme])
                    somme=var_dataset[i][0]
                    i+=1
            

        return(new_dataset)


    def application_regionale(self,dataset):
        var_dataset=(Selection_Var(self.var_selection,'covid').application(dataset)).donnees_covid.liste
        
        liste_region=self.reg()
        donnees_covid=dataset.donnees_covid.liste
        somme=0
        indice_jour=donnees_covid[0].index("jour")
        indice_dep=donnees_covid[0].index("dep")
        

        if 'sexe' in dataset.donnees_covid.liste[0]:

            indice0,indice1,indice2=self.sexe(dataset)
        
            somme0=0
            somme1=0
            somme2=0

            difference1=indice1-indice0
            difference2=indice2-indice0
            difference=indice2-indice0+1
            ind_bon_dep=None

            new_dataset=Dataset(Covid(None,[["Region",'jour',"sexe",self.var_selection]]),dataset.donnees_vacances)
            new_jour=donnees_covid[1][indice_jour]
            for region in liste_region:
                pos0=indice0
                new_jour=donnees_covid[1][indice_jour]
                               
                while pos0<(len(var_dataset)-difference) :
                    jour=donnees_covid[pos0][indice_jour]
                    while jour==new_jour and pos0<(len(var_dataset)-difference) :
                        if donnees_covid[pos0][indice_dep] in region:                 
                                                                       
                            somme0+=var_dataset[pos0][0]
                            somme1+=var_dataset[pos0+difference1][0]
                            somme2+=var_dataset[pos0+difference2][0]
                            ind_bon_dep=pos0
                            pos0+=difference
                            new_jour=donnees_covid[pos0][indice_jour]
                        else: 
                            pos0+=difference
                            new_jour=donnees_covid[pos0][indice_jour] 
                    if ind_bon_dep!=None:
                        new_dataset.ajout_donnees_covid([region[0],donnees_covid[pos0][indice_jour],float(0),somme0])
                        new_dataset.ajout_donnees_covid([region[0],donnees_covid[pos0+difference1][indice_jour],float(1),somme1])
                        new_dataset.ajout_donnees_covid([region[0],donnees_covid[pos0+difference2][indice_jour],float(2),somme2])
                    ind_bon_dep=None
                    somme0=0                       
                    somme1=0
                    somme2=0
                    pos0+=difference
                         
                         

        else:
            new_dataset=Dataset(Covid(None,[["Region",'jour',self.var_selection]]),dataset.donnees_vacances)
            somme=0
            i=1
            new_jour=donnees_covid[i][indice_jour]
            ind_bon_dep=None
            for region in liste_region:
                i=1
                new_jour=donnees_covid[i][indice_jour]
                while i<len(var_dataset)-1:
                    jour=donnees_covid[i][indice_jour]
                    while jour==new_jour and i<len(var_dataset)-1 :
                        if donnees_covid[i][indice_dep] in region :
                                                         
                            somme+=var_dataset[i][0]
                            ind_bon_dep=i
                            i+=1
                            new_jour=donnees_covid[i][indice_jour]
                        else:
                            i+=1
                            new_jour=donnees_covid[i][indice_jour]    
                    if ind_bon_dep!=None:
                        new_dataset.ajout_donnees_covid([region[0],donnees_covid[ind_bon_dep][indice_jour],somme])
                    ind_bon_dep=None
                    somme=0
                    i+=1
                               
            
        return(new_dataset)

    def application_Covid(self,dataset):

        return(self.application_nationale(dataset) if self.granularite.lower()=='nationale' else self.application_regionale(dataset))
    
    def application_Vacance(self,dataset):
        return( "Il n'y a pas d'agrégation spatiale pour les vacances")









