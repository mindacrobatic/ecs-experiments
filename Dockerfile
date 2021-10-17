FROM python:3.9

WORKDIR app
ADD requirements.txt .

RUN apt update & apt dist-upgrade -y & apt install -y gcc

RUN pip install wheel cython
RUN pip install -r requirements.txt

ADD . .

CMD gunicorn --bind 0.0.0.0:5000 api_2.wsgi:app
