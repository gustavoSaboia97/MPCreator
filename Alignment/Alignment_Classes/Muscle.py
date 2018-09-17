#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Descricao          : Control the Muscle program
# AUTOR              : Gustavo Saboia
# DATA               : 22/08/2018
#-------------------------------------------------------------------------------------
import os, subprocess

class Muscle:    
    def __init__(self):
        pass
    #Verify if the alignment was successful
    def verifyAlignment(self,output_file_path):
        exists = os.path.isfile(output_file_path)
        if exists:
            size = os.path.getsize(output_file_path)
            if size != 0:
                return True
        return False


    def align(self,input_file_path,output_dir_path):
        input_file_path = output_dir_path+"/toAlign/"+input_file_path
        #Get the name to create an output file
        split1 = input_file_path.split("/")
        split2 = split1[-1].split(".fasta")
        output_file_path = output_dir_path + "/Alignment/" + split2[0] + ".fasta"

        terminal_string = "muscle -in "+input_file_path+" -out "+output_file_path
        terminal_output = subprocess.getoutput(terminal_string)

        return self.verifyAlignment(output_file_path)