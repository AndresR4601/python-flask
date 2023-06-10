FROM python:3.9

RUN apt-get update && apt-get install -y unixodbc-dev
RUN sudo apt-get update
RUN sudo apt-get install -y msodbcsql17
RUN sudo apt-get install -y apt-utils



ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP run.py
COPY requirements.txt /
RUN pip install -r requirements.txt
COPY . /
CMD flask run -h 0.0.0.0 -p 5000
