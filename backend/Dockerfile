# 
#command

FROM python:3.13.4-slim-bullseye

RUN python3 -m venv /opt/venv/
ENV PATH=/opt/venv/bin:$PATH
WORKDIR /app

COPY requirements.txt /tmp/requirements.txt

RUN /opt/venv/bin/pip install -r /tmp/requirements.txt


COPY ./src .


CMD ["python3","-m","http.server","8000"]