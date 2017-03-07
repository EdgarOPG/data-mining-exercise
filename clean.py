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

def count_photos(data, column):
    temp = []
    for x in range(len(data)):
        temp.append(len(data.iloc[x][column]))
    data[column] = temp
    return data

def create_density_plot(data):
	data.plot(kind='density', subplots=True, layout=(3,3),
		sharex=False)
	plt.show()

def save(data):
    data.to_csv('t.csv', index = False)

if __name__ == '__main__':
    data = open_file('train.json')

    data = count_photos(data, 'photos')

    #show_data_info(data)
    create_density_plot(data)
    save(data);
