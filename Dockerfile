FROM ubuntu:20.04

 RUN apt-get update && apt-get install -y python3-flask

COPY ./app.py /app.py

ENTRYPOINT [ "python3" ]
CMD [ "/app.py" ]