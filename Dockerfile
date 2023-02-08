FROM python:3.8
COPY . /app
WORKDIR /app 
RUN pip install -r requirements.txt 
EXPOSE $PORT 
CMD gunicorn -w 2 --threads 2 --bind 0.0.0.0:$PORT app:app --timeout 1000