import pandas as pd
import matplotlib.pyplot as ptl
import math as mt

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

#Funciona pero la columna necesita no tener campos vacios o programarse para que les asigne 0 a esos
def count_words(data, column):
    temp = []
    array = []
    for x in range(len(data)):
        array = data.iloc[x][column].split(' ')
        temp.append(len(array))
    data[column] = temp
    return data

def save(data):
    data.to_csv('clean_dataset.csv', index = False)

if __name__ == '__main__':
    
    data = open_file('train.json')

    data = count_array_elements(data, 'photos')

    show_data_info(data)

    count_words(data, 'description')

    save(data);
