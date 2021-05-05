import random 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from donnees_covid import Covid
from dataset import Dataset
a = Covid('/Users/thomashilger/Desktop/view.php.csv')
data=Dataset(a)



def nettoyage_dataset(dataset):

    dataset_sortie=dataset
    for ligne in dataset_sortie.donnees_covid.dictionnaire:
        for i in range(len(ligne)-1,-1,-1):
                if not type(ligne[i])== float:
                    del ligne[i]
    return dataset_sortie.donnees_covid.dictionnaire[1:]


def distanceself(X1,X2):
    return (sum(X1-X2)**2)**(0.5)

def findclosestcentroids(ic,X):
    assigned_entroids=[]
    for i in X:
        distance=[]
        for j in ic :
            distance.append(distanceself(i,j))
            assigned_entroids.append(np.argmin(distance))
    return assigned_entroids

def calc_centroids(clusters, X):
    new_centroids = []
    new_df = pd.concat([pd.DataFrame(X), pd.DataFrame(clusters, columns=['cluster'])],
                      axis=1)
    for c in set(new_df['cluster']):
        current_cluster = new_df[new_df['cluster'] == c][new_df.columns[:-1]]
        cluster_mean = current_cluster.mean(axis=0)
        new_centroids.append(cluster_mean)
    return new_centroids



X=np.array(nettoyage_dataset(data))

init_centreoids=random.sample(range(0,len(X)),3)
centroids=[]
for i in init_centreoids:
    centroids.append(X[i])

centroids=np.array(centroids)
get_centroids=findclosestcentroids(centroids,X)

for i in range(4):
    get_centroids = findclosestcentroids(centroids, X)
    centroids = calc_centroids(get_centroids, X)
    
    #plt.figure()
    #plt.scatter(np.array(centroids)[:, 0], np.array(centroids)[:, 1], color='black')
    #plt.scatter(X[:, 0], X[:, 1], alpha=0.1)
    #plt.show()








