# 
#command

FROM python:3.13-slim-bookworm

# host.docker.internal -> localhost
# curl -X POST -d '{"message" : "Hello world "}' -H "Content-Type: application/json" http://host.docker.internal:8080/api/chats
RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*

RUN python3 -m venv /opt/venv/
ENV PATH=/opt/venv/bin:$PATH
WORKDIR /app

COPY requirements.txt /tmp/requirements.txt

RUN /opt/venv/bin/pip install -r /tmp/requirements.txt


COPY ./src .


CMD ["python3","-m","http.server","8000"]