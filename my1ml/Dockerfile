FROM python:3.7-slim-bullseye
RUN apt-get update -y
RUN apt-get install -y libjpeg-dev

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./*.py ./

#CMD [ "python", "./dataVisualization.py" ]
CMD [ "python3"]

# build: docker image build -t my1ml .
# run: docker container run my1ml
# run interactive: docker container run -it my1ml bash