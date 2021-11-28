# My first jupytor

## Epic
As JS I want to learn Jupyter in container so I can use and demonstrate it

Note: Jupyter-stacks in favour of Jupytor-notebook 

### try a container on local Docker
https://jupyter-docker-stacks.readthedocs.io/en/latest/ 
- https://jupyter.org/
- https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html

```
docker container run -p 8888:8888 jupyter/scipy-notebook:python-3.9.7
```
or
```
docker container run -p 8888:8888 jupyter/scipy-notebook:notebook-6.4.5
```
Note: images compressed is 800 MB

Start with: token is given
```
localhost:8888/?token=<>
```
Start in notebook with new and python3

```
docker container run -p 8888:8888 jupyter/scipy-notebook -e JUPYTER_ENABLE_LAB=yes
```

## Resources
https://jupyter.org/  
https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html  
https://github.com/jupyter/docker-stacks  



