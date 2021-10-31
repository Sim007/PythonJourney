FROM python:3.6-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./*.py ./*.py

CMD [ "python", "./makePredictions.py" ]

# build: docker image build -t my1ml .
# run: docker container my1ML