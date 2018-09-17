#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Descricao          : Control the Mafft program
# AUTOR              : Gustavo Saboia
# DATA               : 22/08/2018
#-------------------------------------------------------------------------------------
import os, subprocess

class Mafft:
    def __init__(self):
        pass

    ##Just to know the number of sequences
    def count_sequencies(self,file_to_read):
        try:
            text = open(file_to_read,"r").read()
            return text.count('>')
        except FileNotFoundError:
            pass

    ##Decides which is the best command line 
    def best_command_line(self, input_file,file_name,n_sequencies):
        if n_sequencies < 200:
            terminal_string = "mafft --localpair --maxiterate 1000 "+input_file+" > "+file_name

        elif n_sequencies > 2000:	
            terminal_string = "mafft --retree 1 --maxiterate 0 "+input_file+" > "+file_name
        else:
            terminal_string = "mafft --retree 2 --maxiterate 1000 "+input_file+" > "+file_name

        mafftOutput = subprocess.getoutput(terminal_string)
        del mafftOutput
        
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
        n_sequencies = self.count_sequencies(input_file_path)

        self.best_command_line(input_file_path,output_file_path,n_sequencies)

        return self.verifyAlignment(output_file_path)