FROM python:3.7
WORKDIR /
RUN apt-get update && \
    apt-get -y install gcc mono-mcs && \
    apt-get -y install python-dev && \
    apt-get -y install librdkafka-dev libpq-dev python3-dev
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt