#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Descricao          : Control output screen
# AUTOR              : Gustavo Saboia
# DATA               : 22/08/2018
#-------------------------------------------------------------------------------------
import sys

class Interface:
    def __init__(self):
        pass
    
    def genbank_extraction_outputs(self,first_time,id,condition):
        if first_time:
            print("======Downloading the Files=======")
        else:
            if condition:
                print("Name: "+ id + " --> Done")
            else:
                print("Name: "+ id + " --> Error")
    