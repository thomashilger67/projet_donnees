from estimation_descriptive import Estimation
from dataset import Dataset 
import random 
import numpy as np
import pandas as pd
from donn

def distance(X1,X2):
    return (sum(X1-X2)**2)**(0.5)

def findclosestcentroids(ic,X):
    assigned_entroids=[]
    for i in X:
        distance=[]
        for j in ic :
            distance.append(distance(i,j))
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

class EstimationMultivariee(Estimation):

    def __init__(self):
        pass


    def Kmeans(self, dataset,k):
        X=np.array(dataset.donnees_covid.dictionnaire)
        init_centreoids=random.sample(range(0,len(X)),k)
        centroids=[]
        for i in init_centreoids:
            centroids.append(X[i])

        centroids=np.array(centroids)
        get_centoids=findclosestcentroids(centroids,X)

        for i in range(10):
            get_centroids = findClosestCentroids(centroids, X)
            centroids = calc_centroids(get_centroids, X)
    
            plt.figure()
            plt.scatter(np.array(centroids)[:, 0], np.array(centroids)[:, 1], color='black')
            plt.scatter(X[:, 0], X[:, 1], alpha=0.1)
            plt.show()








