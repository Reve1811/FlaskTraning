FROM python:latest

RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
RUN apt-get update 
RUN apt-get install -y git tzdata

RUN apt-get install -y vim
RUN apt-get install -y git
    
