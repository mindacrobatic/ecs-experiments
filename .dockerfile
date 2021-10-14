FROM python:3.9

WORKDIR app
ADD requirements.txt

RUN apt update & apt upgrade -y | apt install -y gcc python3-devel

RUN python3 install wheel cython
RUN python3 -y install -r requirements.txt

ADD .

RUN gunicorn --bind 0.0.0.0:5000 api_2.wsgi:app
