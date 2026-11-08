
#command

FROM python:3.13.4-slim-bullseye

WORKDIR /app

#COPY local_folder destination folder
# RUN mkdir -p /static_folder
#COPY .static_html static_folder

# same destination is /app
# COPY ./static_html /app
COPY ./src .

# RUN echo "hello" > index.html

#docker build-f dockerfile -t pyapp .
#docker run -it pyapp

#docker build-f Dockerfile -t aniketmani/ai-py-app:v1
#docker push aniketmani/ai-py-app:v1

#python -m http.server 8000
#docker run -it -p 3000:8000 pyapp
CMD ["python3","-m","http.server","8000"]