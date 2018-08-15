FROM ubuntu:18.04

MAINTAINER Gustavo Saboia

RUN set -x \
    && apt-get update \
    && apt-get install -y \
#Tools
        nano git \
#Dependecies
        python3 mafft muscle t-coffee clustalw ncbi-entrez-direct
    
#Preparing to get the MPCreator
CMD set -x \
    && apt-get install wget zip unzip -y \
    && wget https://github.com/gustavoSaboia97/MPCreator/archive/master.zip \
    && unzip master.zip \
    && mv /MPCreator-master /root/MPCreator \
    && rm /master.zip

#Getting inside the directory of MPcreator
WORKDIR /root/MPCreator


