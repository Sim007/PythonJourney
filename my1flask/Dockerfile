FROM python:3.9-alpine
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY ./app/*.* .
CMD ["python3","hello.py"]

#Build:              docker image build -t my1flask .
#Run  :              docker container run -p 5000:5000 my1flask
#Debug in container: docker container run -it my1flask sh