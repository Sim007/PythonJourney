# Introduction
In this folder of repo, my journey learning ML and my thoughts of using containers.  

For this I have found a nice article on the internet which I will use to learn ML and use containers,

## Resource
I use the following excellent resource:  
https://machinelearningmastery.com/machine-learning-in-python-step-by-step/ 
Many thanks for sharing!

## Workflow according article
A machine learning project may not be linear, but it has a number of well known steps:  

- Define Problem.
- Prepare Data.
- Evaluate Algorithms.
- Improve Results.
- Present Results.

## Userstory
High Level: Bake a container for this examples of the article - so you focus on learning ML and not having trouble of installing and not having the correct versions. 

As student I want to have a container environment that I can use for production so I can share my work to other people

### Way of thinking
design decision for this user story:
- no jupyter notebook because my opioun is that the jupyter notebook is not a production thingie
- source in GitHub
- edit in Visual Studio on laptop
- 1 container run on Docker
  - Dockerfile
  - Docker container image on DockerHub
  - Semantic versioning: Major.Minor.Patch-YYYYMMDDHHMM

## Run the exmples on a laptop

First step run the examples of the article.   
I do this on with Linux box on chromebook  

### Dependencies
The examples needs the following dependecies:
- Python 3.x
- Libs:  
  - scipy
  - numpy
  - matplotlib
  - pandas
  - sklearn  

### Installation
- python 3.6 installed
- made dir my1ML

All completed scripts I copied to this repo, tweaked them for my purpose, so I can use them.  
So I can copy the script on my machine and run the script.

```
curl https://raw.githubusercontent.com/Sim007/PythonJourney/main/my1ML/checkenv.py > checkenv.py  
python3 checkenv.py
```
sklearn niet aanwezig
```
pip3 install -U scikit-learn
```
Veroudere versie van pip3
```
python3 -m pip install --upgrade pip
```
Output:
Python: 3.7.3 (default, Jan 22 2021, 20:04:44) 
[GCC 8.3.0]  
scipy: 1.6.2  
numpy: 1.18.4  
matplotlib: 3.4.1  
pandas: 1.3.3  
sklearn: 1.0  

## Scripts

### Load DataSet
- copy of https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv as iris.csv in repo  
- See also wiki: https://en.wikipedia.org/wiki/Iris_flower_data_set   

```
curl https://raw.githubusercontent.com/Sim007/PythonJourney/main/my1ML/loadDataSet.py > loadDataSet.py
python3 loadDataSet.py
```

### Summarize Dataset
```
curl https://raw.githubusercontent.com/Sim007/PythonJourney/main/my1ML/summarizeData.py > summarizeData.py
python3 summarizeData.py
```

### Data Visulalization
```
curl https://raw.githubusercontent.com/Sim007/PythonJourney/main/my1ML/dataVisualization.py > dataVisualization.py
python3 dataVisualization.py
```
Script will show 3 graph. Exit to see to following graph.

## Evaluate some algorithms
Steps in script:

- Separate out a validation dataset.
- Set-up the test harness to use 10-fold cross validation.
- Build multiple different models to predict species from flower measurements
- Select the best model.

```
curl https://raw.githubusercontent.com/Sim007/PythonJourney/main/my1ML/evalSomeAlgorithms.py > evalSomeAlgorithms.py
python3 evalSomeAlgorithms.py
```
---


