import pandas as pd
import random

def euclidean_distance(x, y):
    return abs(x - y)

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

def kmean(data, k):
    # Choose k random value
    arr_rnd_center = []
    for rnd in range(k):
        rnd = random.randint(0, data.shape[0])
        arr_rnd_center.append(data.iloc[[rnd]])
    for elem in arr_rnd_center:
        print(elem)


def cluster_male(data):
    data = choose_male(data)
    data = retrieve_gold_medal(data)
    data = retrieve_basketball(data)
    data = data[data['Year'] >= 1980]
    k = 3 # Nb Cluster (taille petite, taille moyenne, taille grande)
    kmean(data, k)
    

if __name__ == "__main__":
    data = retrieve_data()
    data = clean_data(data)
    cluster_male(data)