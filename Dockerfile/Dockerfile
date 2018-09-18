FROM ubuntu:18.04

RUN apt-get update \
    #TOOLS
    && apt-get install -y nano git \
    #DEPENDENCIES 
    && apt-get install -y python3 mafft muscle t-coffee ncbi-entrez-direct

RUN set -x & git clone https://github.com/gustavoSaboia97/MPCreator.git /app

WORKDIR /app
