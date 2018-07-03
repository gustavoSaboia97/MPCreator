#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Descricao          : Read the IDs in a file
# AUTOR              : Gustavo Saboia
# DATA               : 29/04/2018
#-------------------------------------------------------------------------------------
import os;

class FileReader:
    def __init__(self):
        self.finalList = list();
        pass;

    def readFile(self,filePath):
        filePath = os.path.abspath(filePath);
        f = open(filePath,"r");
        dataFile = f.read();
        
        vector = dataFile.split("\n");
        
        for i in range(0,len(vector)):
            self.finalList.append(vector[i].replace(" ",""));
            
        return self.finalList;