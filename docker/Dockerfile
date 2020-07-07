FROM python:3.6

EXPOSE 5000

WORKDIR /

COPY app .

COPY docker/requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD [ "python3", "-u", "main.py" ]