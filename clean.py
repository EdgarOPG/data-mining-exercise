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

def fill_missing_values_with_mean(data, column):
    temp = data[column].fillna(data[column].mean())
    data[column] = temp
    return data

def fill_missing_values_with_mode(data, column):
    temp = data[column].fillna(data[column].mode()[0])
    data[column] = temp
    return data

#Funciona pero la columna necesita no tener campos vacios o programarse para que les asigne 0 a esos
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

    data = count_array_elements(data, 'photos')
    data = count_array_elements(data, 'features')    
    count_words(data, 'description')
    show_data_info(data)
    save(data[:500]);
