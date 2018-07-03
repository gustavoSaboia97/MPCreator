#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Descricao          : Receive the IDs
# AUTOR              : Gustavo Saboia
# DATA               : 29/04/2018
#-------------------------------------------------------------------------------------
from ControleArquivo import ControleArquivo;
from DMitocondria import DMitocondria;
from Alinhamento import Alinhamento;
from FileReader import FileReader;
import sys;

ca = ControleArquivo();

ca.criarDirResultados();

try:
    filePath = sys.argv[1];
    fileReader = FileReader();
    ids = fileReader.readFile(filePath);
except IndexError:
    while (True):
        ##Getting the IDs, to download the sequences
        print("Put the ID(s)");
        print("Separating them by commas. EX: 123,321,432");
        string = str(input("Sequences:" ));

        ##Validating the IDs to create a mitocondrial process
        ids = string.split(",");
        if (len(ids) > 1 ):
            break;
        else:
            continue;

print("Welcome to MPCreator!");

instance = DMitocondria();


filesString = instance.executar("Nucleotide",ids);
dirMitocondria = instance.retornarCaminho();
dirName = instance.returnDirName();

del instance;

if (filesString != None):
    alignment = Alinhamento();

    files = filesString.split(",");

    op = alignment.menu();

    if op == 1:
        print("Creating an alignment with Mafft");
    if op == 2:
        print("Creating an alignment with Muscle");
    if op == 3:
        print("Creating an alignment with ClustalW");
    if op == 4:
        print("Creating an alignment with T_Coffee");
    
    for i in range(0,len(files)-1):
        alignment.escolhaAlinhamento(op,files[i],dirName);

    ca.concatenarMitocondria(dirMitocondria,"rRNA");
    ca.concatenarMitocondria(dirMitocondria,"tRNA");
    ca.concatenarMitocondria(dirMitocondria,"CDS");
    #ca.concatenarMitocondria(dirMitocondria,"gene");
    ca.concatenarMitocondria(dirMitocondria,"D-loop");

    print("Results in ~/MPResults/"+dirName+"/FinalAlignment");

    





		