#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Descricao          : Start the Mithocondria Modules
# AUTOR              : Gustavo Saboia
# DATA               : 22/08/2018
#-------------------------------------------------------------------------------------
import sys

class Errors:
    def __init__(self):
        pass
    
    def error(self,error):
        print("Error: "+error)
        sys.exit()
    
    def non_stopable_error(self,error):
        print("Message: "+error)

    def file_quantity_error(self):
        error = "You need at least two files"
        self.error(error)

    def download_error(self):
        error = "There was errors downloading the sequences"
        self.error(error)
    
    def reading_error(self):
        error = "There was errors reading the sequences"
        self.error(error)
    
    def parameter_init_error(self):
        error = "You can choose only one of these parameters: \'-i\' \'-d\'\nBecause they work with the same methods. \'-i\' indicates to download by referencing a file with ids of NCBI\nand \'-d\' indicates a directory with mithocondry Genbank files"
        self.error(error)

    def parameter_obligatory_error(self):
        error = "You must use the complementary parameters: \n \'-o\' to name the output folder and \'-a\' to indicate the alignment program"
        self.error(error)

    def parameter_error(self):
        error = "The terminal command isn't right\n \'-f\' FILE_PATH\n\n \'-d\' DIR_PATH\n\n \'-a\' ALIGNMENT_PROGRAM_ID\n\n \'-o\' OUTPUT_FOLDER_NAME\n"
        self.error(error)

    def user_result_folder_exists(self,folder_path):
        error = "The user result folder already exists -> "+folder_path
        self.error(error)

    def result_folder_exists(self):
        error = "The Result Folder Exists"
        self.non_stopable_error(error)

