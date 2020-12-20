import pandas as pd
import random
import numpy as np
import csv

def euclidean_distance(x, y):
    return abs(x - y)

def calculate_mean(heights):
    if (len(heights) > 0):
        return sum(heights) / len(heights)
    return 0

def retrieve_data():
    filename = '../dataset/data.csv'
    return pd.read_csv(filename)

def clean_data(data):
    del data['NOC']
    del data['Games']
    del data['Weight']
    del data['Event']
    del data['City']
    del data['Age']
    del data['Season']
    del data['Name']
    del data['Team']
    data = data[data['Height'].notna()]
    return data

def choose_male(data):
    return data[data['Sex'] == 'M']

def choose_female(data):
    return data[data['Sex'] == 'F']

def retrieve_gold_medal(data):
    return data[data['Medal'] == 'Gold']

def retrieve_basketball(data):
    return data[data['Sport'] == 'Basketball']


def choose_cluster_center_rnd(data, k):
    arr_rnd_center = []
    for rnd in range(k):
        rnd = random.randint(0, data.shape[0])
        arr_rnd_center.append(data.iloc[rnd]['Height'])
    return arr_rnd_center

def determine_new_centroids(result_cluster, k):
    new_centroids = []
    for idx in range(k):
        new_centroids.append(calculate_mean(result_cluster[idx + 1]))
    return new_centroids

def csv_result(clusters_ids):
    with open('result.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, clusters_ids.keys())
        writer.writeheader()
        writer.writerow(clusters_ids)

def handle_define_cluster(data, center_clusters, k):
    result_cluster = dict()
    result_cluster_ids = dict();
    for idx in range(k):
        result_cluster[idx + 1] = []
        result_cluster_ids[idx + 1] = []
    for row_idx in range(data.shape[0]):
        pBest = 1000.0
        index_cluster = -1
        for idx, elem in enumerate(center_clusters):
            distance = euclidean_distance(elem, data.iloc[row_idx]['Height'])
            if (distance.item() < pBest):
                pBest = distance.item()
                index_cluster = idx + 1
        result_cluster[index_cluster].append(data.iloc[row_idx]['Height'])
        result_cluster_ids[index_cluster].append(data.iloc[row_idx]['ID'])
    csv_result(result_cluster_ids)
    return result_cluster

def determine_end_kmean(centroids, new_centroids, k):
    res = 0
    for c in range(len(centroids)):
        if round(centroids[c], 3) == round(new_centroids[c], 3):
            res += 1
    if res == k:
        return 0
    return -1

def kmean(data, k):
    result_cluster = dict()
    center_clusters = choose_cluster_center_rnd(data, k)
    for idx in range(k):
        result_cluster[idx + 1] = []
    tmp_old_cluster = []
    while determine_end_kmean(tmp_old_cluster, center_clusters, k) == -1:
        result_cluster = handle_define_cluster(data, center_clusters, k)
        tmp_old_cluster = center_clusters
        center_clusters = determine_new_centroids(result_cluster, k) 
    print(result_cluster)
            

def cluster_m(data):
    data = choose_male(data)
    data = retrieve_gold_medal(data)
    data = retrieve_basketball(data)
    data = data[data['Year'] >= 1950]
    k = 3 # Nb Cluster (taille petite, taille moyenne, taille grande)
    kmean(data, k)

def cluster_f(data):
    data = choose_female(data)
    data = retrieve_gold_medal(data)
    data = retrieve_basketball(data)
    data = data[data['Year'] >= 1950]
    k = 3 # Nb Cluster (taille petite, taille moyenne, taille grande)
    kmean(data, k)
    

if __name__ == "__main__":
    data = retrieve_data()
    data = clean_data(data)
    cluster_m(data)
    cluster_f(data)