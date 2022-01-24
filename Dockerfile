FROM python:alpine3.14
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src src
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=5 CMD curl -f https://localhost:5000/health || exit 1
ENTRYPOINT [ "python", "./src/app.py" ]