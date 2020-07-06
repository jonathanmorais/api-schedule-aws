FROM python:3.6

EXPOSE 5000

WORKDIR /app

COPY . .

COPY docker/requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD [ "python", "-u", "main.py" ]