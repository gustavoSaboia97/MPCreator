FROM ubuntu:18.04

MAINTAINER Gustavo Saboia

RUN set -x \
    && apt-get update \
    && apt-get install -y \
#Tools
        nano git \
#Dependecies
        python3 mafft muscle t-coffee clustalw ncbi-entrez-direct

RUN set -x \
    && git clone https://github.com/gustavoSaboia97/MPCreator.git /root/MPCreator

#Getting inside the directory of MPcreator
WORKDIR /root/MPCreator


