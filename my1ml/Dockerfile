FROM python:3.7-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./*.py ./

#CMD [ "python", "./makePredictions.py" ]
CMD [ "python3"]

# build: docker image build -t my1ml .
# run: docker container my1ml
# run interactive: docker container run -it my1ml bash