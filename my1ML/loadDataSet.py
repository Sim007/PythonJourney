#!/usr/bin/env python3
# script summarizeData
print("*** Script summarizeData.py ***")


# summarize the data
from pandas import read_csv

# Load dataset
# url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
url = https://raw.githubusercontent.com/Sim007/PythonJourney/main/my1ML/summarizeData.py
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)

# shape
print("*** Shape ***)
print()
print(dataset.shape)
print()
print()

# head
print("*** Head ***)
print()
print(dataset.head(20))
print()
print()

# descriptions
print("*** Discription ***)
print()
print(dataset.describe())
print()
print()

# class distribution
print("*** Class distribution ***)
print()
print(dataset.groupby('class').size())
print()
print()
