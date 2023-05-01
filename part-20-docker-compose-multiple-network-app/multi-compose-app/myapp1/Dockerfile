
FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
run pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
run apk add curl
EXPOSE 5002
COPY . .
CMD ["flask", "run"]