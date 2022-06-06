FROM python:3.9.8 AS py3
FROM openjdk:8

WORKDIR /src

COPY src/ .
COPY requirements.txt .

COPY --from=py3 / /

RUN pip install -r requirements.txt
RUN curl https://s3.amazonaws.com/products-42matters/test/biographies.list.gz --output text.gz
RUN gzip -d text.gz

CMD [ "python", "./wordcount.py" ]