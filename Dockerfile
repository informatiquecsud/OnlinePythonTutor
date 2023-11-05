FROM python:3.11-slim-bookworm

ENV PORT=5000
ENV APP_LOCATION=docker
ENV HOST=0.0.0.0

COPY requirements.txt ./

WORKDIR /v5-unity

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python", "bottle_server.py"]