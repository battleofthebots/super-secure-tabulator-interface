FROM ghcr.io/battleofthebots/botb-base-image:latest

USER user
COPY ./app.py .
CMD python3 /app.py

HEALTHCHECK --interval=10s --timeout=5s --start-period=10s --retries=3 \
    CMD [ $(curl -I -s http://0.0.0.0:80 | head -n 1 | cut -d' ' -f2 | head -n 1) -eq 200 ] || exit 1
