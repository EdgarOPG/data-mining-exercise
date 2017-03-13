import pandas as pd
import matplotlib.pyplot as plt
import math as mt
import numpy as np
from pandas.tools.plotting import scatter_matrix

dict = {'low' : 1,
        'medium' : 2,
        'high': 3}

def open_file(fileName):
    data = pd.read_json(fileName)
    return data

def show_data_info(data):
    print("Number of instance:" + str(data.shape[0]))
    print("Number of features:" + str(data.shape[1]))
    print("------------------------------------------")

    print("Initial instance:\n")
    print(data.head(10))

    print("Numerical info:\n")
    numerical_info = data.iloc[:, :data.shape[1]]
    print(numerical_info.describe())

def count_array_elements(data, column):
    temp = []
    for x in range(len(data)):
        temp.append(len(data.iloc[x][column]))
    data[column] = temp
    return data

def fill_missing_values_with_mean(data, column):
    temp = data[column].fillna(data[column].mean())
    data[column] = temp
    return data

def fill_missing_values_with_mode(data, column):
    temp = data[column].fillna(data[column].mode()[0])
    data[column] = temp
    return data

def number_photos_influence_interest_level(data):

    numbPhotos = data['photos'].value_counts()
    numbPhotosKeys = numbPhotos.keys()
    interestArray = []

    for number in numbPhotosKeys:
        subset = data.loc[data['photos'] == number]
        print('Numero de fotos:' + str(number))
        print(subset['interest_level'])
        interestArray.append(subset["interest_level"].mean())

    print(numbPhotosKeys)
    print(interestArray)

    width = .2
    plt.bar(numbPhotosKeys, interestArray, width, color="blue")

    plt.ylabel('nivel de interes')
    plt.xlabel('#fotos')
    plt.title('Numero de fotos influye nivel de interes')
    plt.xticks(np.arange(0, max(numbPhotosKeys), 3))
    plt.yticks(np.arange(0, 3, 1))

    plt.show()

def len_description_influence_interest_level(data):

    numbPhotos = data['description'].value_counts()
    numbPhotosKeys = numbPhotos.keys()
    interestArray = []

    for number in numbPhotosKeys:
        subset = data.loc[data['description'] == number]
        print('Longitud de la descripcion:' + str(number))
        print(subset['interest_level'])
        interestArray.append(subset["interest_level"].mean())

    print(numbPhotosKeys)
    print(interestArray)

    width = .2
    plt.bar(numbPhotosKeys, interestArray, width, color="blue")

    plt.ylabel('nivel de interes')
    plt.xlabel('Longitud de la descripcion')
    plt.title('Longitud de la descripcion influye nivel de interes')
    plt.xticks(np.arange(0, max(numbPhotosKeys), 40))
    plt.yticks(np.arange(0, 3, 1))

    plt.show()

def number_features_influence_price(data):

    numbFeatures = data['features'].value_counts()
    numbFeaturesKeys = numbFeatures.keys()
    priceArray = []

    for number in numbFeaturesKeys:
        subset = data.loc[data['features'] == number]
        print('Numero de caracteristicas:' + str(number))
        print(subset['price'])
        priceArray.append(subset["price"].mean())

    print(numbFeaturesKeys)
    print(priceArray)

    width = .2
    plt.bar(numbFeaturesKeys, priceArray, width, color="blue")

    plt.ylabel('Precio')
    plt.xlabel('#caracteristicas')
    plt.title('Numero de caracteristicas influye precio')
    plt.xticks(np.arange(0, max(numbFeaturesKeys), 2))
    plt.yticks(np.arange(0, 15000, 1000))

    plt.show()

def count_words(data, column):
    temp = []
    for x in range(len(data)):
        if(data.iloc[x][column] == '        '):
            temp.append(0)
        else:
            temp.append(len(data.iloc[x][column].split(' ')))
    data[column] = temp
    return data

def save(data):
    data.to_csv('clean_dataset.csv', index = False)

if __name__ == '__main__':

    data = open_file('train.json')
    data['interest_level'] = data['interest_level'].replace(dict)
    data = count_array_elements(data, 'photos')
    data = count_array_elements(data, 'features')
    data = count_words(data, 'description')
    len_description_influence_interest_level(data)
    #number_photos_influence_interest_level(data)
    #number_features_influence_price(data)
    #show_data_info(data)
    #save(data[:500]);
