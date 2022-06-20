FROM python:3

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY config.py ./config.py
COPY inference.py ./inference.py
COPY model.h5 ./model.h5
COPY tokenizer.joblib ./tokenizer.joblib

CMD [ "python", "./inference.py" ]