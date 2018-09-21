#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Descricao          : Start the Mithocondria Modules
# AUTOR              : Gustavo Saboia
# DATA               : 22/08/2018
#-------------------------------------------------------------------------------------
from Classes.Errors import Errors 
import os

class SystemControl:
    def __init__(self):
        self.errors = Errors()
        pass

    #It Creates gb files to save which file were downloaded 
    def create_gb_files(self,gbNames,gbFiles,output_dir_path):
        i = 0
        for gbFile in gbFiles:
            file_open = open(output_dir_path+"/GenbankFiles/"+gbNames[i]+".gb","w")
            file_open.write(gbFile)
            file_open.close()
            i += 1

###########################################################
############# GENERATE PATERN FOLDERS #####################
###########################################################
    def generate_main_results_folder(self,path):
        try:
            os.mkdir(path)
        except FileExistsError:
            self.errors.result_folder_exists()

    def generate_gb_folder(self,path):
        try:
            os.mkdir(path+"/GenbankFiles")
        except FileExistsError:
            # self.errors.user_result_folder_exists(path)
            pass
           
    def generate_results_folder(self,path):
        try:
            os.mkdir(path)
            os.mkdir(path+"/toAlign")
            os.mkdir(path+"/Alignment")
            os.mkdir(path+"/FinalAlignment")
        except FileExistsError:
            # self.errors.user_result_folder_exists(path)
            pass
            
###########################################################