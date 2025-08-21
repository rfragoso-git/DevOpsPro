FROM python:3.13.3-alpine3.20

WORKDIR /usr/src/app

RUN pip install --upgrade pip

COPY hello_word_v2.py ./

CMD [ "python", "./hello_word_v2.py" ]

EXPOSE 8585