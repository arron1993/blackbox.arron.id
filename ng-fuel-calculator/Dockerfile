FROM node:12.21.0-alpine3.10 as angular_build

RUN npm install -g @angular/cli


RUN mkdir /ng-fuel-calculator
COPY ./package.json /ng-fuel-calculator

WORKDIR /ng-fuel-calculator
RUN npm install
RUN npx ngcc

COPY ./src /ng-fuel-calculator/src
COPY ./dist /ng-fuel-calculator/dist
COPY ./angular.json /ng-fuel-calculator
COPY ./tsconfig.app.json /ng-fuel-calculator
COPY ./tsconfig.json /ng-fuel-calculator
# RUN npm run build-prod

FROM nginx:latest

COPY --from=angular_build /ng-fuel-calculator/dist /usr/share/nginx/html

