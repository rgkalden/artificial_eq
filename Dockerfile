FROM python:3

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY inference.py ./inference.py
COPY baseline-glove-2022-04-28-19-08-04-test-acc-0.505.h5 ./baseline-glove-2022-04-28-19-08-04-test-acc-0.505.h5
COPY tokenizer.joblib ./tokenizer.joblib

CMD [ "python", "./inference.py" ]