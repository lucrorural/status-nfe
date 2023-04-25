FROM python:3.9

ENV PYTHONUNBUFFERED 1

LABEL name="statusnfe"
LABEL version="0.0.1"
LABEL description="Status NFe"
LABEL org.lucrorural.vendor="Lucro Rural"

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . /app/
WORKDIR /app/

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "proj.wsgi:application", "-k", "gevent"]