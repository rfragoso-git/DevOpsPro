FROM ubuntu:20.04

LABEL Author="Renato O. Fragoso"

LABEL Email="rof1966@hotmail.com"

RUN apt update && apt install curl wget vim -y 

ENV VLR_DOCKER_ENV=" Valor é Docker !!!"

WORKDIR /app

COPY --chown=root:root --chmod=755 test.txt .

ADD arq.tar.gz /app

VOLUME [ "/worker" ]

ARG VAR_MSG="Bem vindo ao universo Docker"

RUN echo $VAR_MSG > msg.txt

# ADD https://learn.microsoft.com/pt-br/plans/odgoumz8rnrmxz?sharingId=CEACA73C9FB6C5EA&source=docs curso_microsoft.html


