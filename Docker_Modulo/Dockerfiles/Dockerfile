FROM node:20.19-alpine3.21

WORKDIR /app

COPY src/package*.json .

RUN npm install

COPY src/  .

EXPOSE 8080

CMD [ "node", "server.js" ]

