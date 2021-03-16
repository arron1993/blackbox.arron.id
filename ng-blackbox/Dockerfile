FROM node:12.21.0-alpine3.10 as angular_build

RUN npm install -g @angular/cli


RUN mkdir /ng-blackbox
COPY ./package.json /ng-blackbox

WORKDIR /ng-blackbox
RUN npm install
RUN npx ngcc

COPY ./src /ng-blackbox/src
#COPY ./dist /ng-blackbox/dist
COPY ./angular.json /ng-blackbox
COPY ./tsconfig.app.json /ng-blackbox
COPY ./tsconfig.json /ng-blackbox
RUN ng build --prod

FROM nginx:latest

COPY --from=angular_build /ng-blackbox/dist /usr/share/nginx/html

