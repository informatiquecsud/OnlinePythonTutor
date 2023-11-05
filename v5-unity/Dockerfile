FROM python:3.12-slim

ENV PORT=5000
ENV APP_LOCATION=docker
ENV HOST=0.0.0.0

WORKDIR /app
COPY * ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE ${PORT}

CMD [ "python", "bottle_server.py"]