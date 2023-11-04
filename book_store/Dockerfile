FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /application
COPY requirements.txt /application/
RUN pip install -r requirements.txt

ADD . .
RUN chown -R root:root static media

COPY . /application/
