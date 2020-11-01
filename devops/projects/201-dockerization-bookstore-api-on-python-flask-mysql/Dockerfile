FROM python:alpine
COPY . .
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 80
CMD python ./bookstore-api.py