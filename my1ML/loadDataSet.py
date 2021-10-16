#!/usr/bin/env python3

# Load dataset
# original location
# url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
url = "https://raw.githubusercontent.com/Sim007/PythonJourney/main/my1ML/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)
