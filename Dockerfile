FROM ubuntu:20.04

 RUN apt-get update && apt-get install -y python3-flask

COPY ./app.py /app.py

ENTRYPOINT [ "python3" ]
CMD [ "/app.py" ]
HEALTHCHECK --interval=10s --timeout=5s --start-period=10s --retries=3 \
    CMD [ $(curl -I -s http://0.0.0.0:80 | head -n 1 | cut -d' ' -f2 | head -n 1) -eq 200 ] || exit 1
