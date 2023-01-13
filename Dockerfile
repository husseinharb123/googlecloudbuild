FROM python:3-alpine

WORKDIR /app

COPY requirements.txt /app


RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "-m", "app" ]