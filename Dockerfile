FROM python:3.3-alpine

RUN mkdir /home/silos
ADD Scripts/replication.py /home/silos/
WORKDIR /home/silos

ENTRYPOINT ["python", "replication.py"]
