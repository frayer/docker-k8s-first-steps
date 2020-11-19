FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt && \
    rm requirements.txt

COPY app.py .
COPY ./arguments ./arguments

CMD [ "python", "./app.py" ]
