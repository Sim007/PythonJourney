#!/usr/bin/env python3
# script loadDataSet

# summarize the data
from pandas import read_csv

# Load dataset
# url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
url = "https://raw.githubusercontent.com/Sim007/PythonJourney/main/my1ml/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)
