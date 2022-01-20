FROM python:3.9.10-slim

RUN pip3 install python-binance

WORKDIR /app
ADD exchanges /app/exchanges
ADD main.py /app/main.py

ENTRYPOINT ["python3", "./main.py"]
