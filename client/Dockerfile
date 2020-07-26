FROM node:14.5.0-stretch

RUN npm install -g http-server
WORKDIR /client
COPY package*.json ./
RUN npm install
COPY . .
ENV VUE_APP_FLASK_API=127.0.0.1
RUN npm run build

EXPOSE 8080
CMD [ "http-server", "dist" ]