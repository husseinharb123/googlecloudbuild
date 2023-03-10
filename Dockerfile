FROM python:3-alpine

WORKDIR /

COPY requirements.txt . 

RUN pip install -r requirements.txt 

COPY . . 

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["app.py"]