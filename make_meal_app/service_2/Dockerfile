FROM python:3.9.6

WORKDIR /service_2

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]