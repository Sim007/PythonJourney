# My ML in k8s

## Goal
Journey: bringing the correct ML to real customers
- ML workflow
- ML in containers
- ML expirements
- ML in production

## Mindset
- Develop ML on local plus
- Share result
- CI/CD pipeline to production
- observability

### Challenges
- where is the data
- test (shadow environment - A/B)
- tracing & auditing
- ML is a part of product
- completeness versus time

## Demo in AI en testen workinggroup

## Why containers?

## Voorbeeld containers
### Voorbeelden
#### jupyter 
Why a notebook?
- easy start
- code + documentation
Why not: 
- ML people smart, why not learn the essentials of prthon, software engineering and CI/CD?
- Learn the real stuff in small steps
see also: https://github.com/Sim007/PythonJourney/tree/main/my1jupyter 
```
docker run -p 8888:8888 jupyter/scipy-notebook:notebook-6.4.5
```
### Test container
A test can also be package in a container - so you can start it from a pipline. 
The test container test contains:
- testframework
- testscript
- test execution
- execution report
- export result + report

#### testcontainer with cypress
...

### datacontainer
...

### Base images
https://docs.microsoft.com/en-us/azure/machine-learning/concept-prebuilt-docker-images-inference

## workflow in k8s CI/CD MLOPS
  - train + production
  - test
  - kubeflow

### Resources
#### ML
https://scikit-learn.org/    
https://data-science-academy3.teachable.com/courses/enrolled/795489  
https://developers.google.com/machine-learning/crash-course  
https://docs.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment 

#### CI/CD MLOPS
https://www.phdata.io/blog/the-ultimate-mlops-guide-how-to-deploy-ml-models-to-production/
https://ml-ops.org/ 
https://www.kubeflow.org/ 
https://github.com/Azure/azureml-examples  
https://docs.microsoft.com/en-us/azure/machine-learning/?view=azure-ml-py  
https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning 
https://martinfowler.com/articles/cd4ml.html
https://developers.google.com/machine-learning/crash-course
https://towardsdatascience.com/ml-ops-machine-learning-as-an-engineering-discipline-b86ca4874a3f
https://proceedings.neurips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf



