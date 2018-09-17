#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Descricao          : Control the Parameters direction
# AUTOR              : Gustavo Saboia
# DATA               : 23/08/2018
#-------------------------------------------------------------------------------------
from Classes.SystemControl import SystemControl
from Classes.Errors import Errors
from Mitochondria.MitochondriaControl import MitochondriaControl
import os

class Parameter:
    def __init__(self):
        self.errors = Errors()
        self.sys_control = SystemControl()
        self.mit_control = MitochondriaControl()
        self.RESULTS_FOLDER = ""
        self.OUTPUT_DIR_PATH = ""
        self.INPUT_FILE_PATH = ""
        self.ALIGNMENT_PROGRAM_ID = ""
        self.INPUT_DIR_PATH = ""

    #INITIALIZE THE VARIABLES WITH THE PARAMETERS
    def get_parameters(self,argv):
        ##SET THE RESULTS FOLDER
        results_dir = os.path.abspath(argv[0])
        self.RESULTS_FOLDER = results_dir.replace("/MPCreator.py","")+"/MPResults"
        #GENERATE THE RESULTS FOLDER
        self.sys_control.generate_main_results_folder(self.RESULTS_FOLDER)

        ##VERIFY THE PARAMETERS AND ACTIONS
        i = 0
        try:
            for p in argv:
                ##ID FILE PARAMETER
                if p == "-f":
                    self.INPUT_FILE_PATH = argv[i+1]
                    
                ##LOCAL FILES PARAMETER, INDICATES A DIRECTORY
                if p == "-d":
                    self.INPUT_DIR_PATH = argv[i+1]

                ##OUTPUT DIRECTORY NAME ONLY THE NAME NOT THE PATH
                if p == "-o":
                    self.OUTPUT_DIR_PATH = self.RESULTS_FOLDER+"/"+argv[i+1]

                ##ALIGNMENT PROGRAM ID
                if p == "-a":
                    self.ALIGNMENT_PROGRAM_ID = argv[i+1]
                
                i += 1
        except IndexError:
            self.errors.parameter_error()

    ##BY COMPARING THE PARAMETERS GET THE WAY THE PROGRAM SHOULD EXECUTE
    def run_application(self):
        ##IF THE USER INPUT DATA FOR ID FILE AND A DIRECTORY WITH FILES
        if self.INPUT_FILE_PATH != "" and self.INPUT_DIR_PATH != "":
            self.errors.parameter_init_error()
        
        ##IF THE USER INPUT DATA FOR ID FILE AND DONT INPUT FOR DIRECTORY WITH FILES
        elif self.INPUT_FILE_PATH != "" and self.INPUT_DIR_PATH == "":
            if self.OUTPUT_DIR_PATH != "" and self.ALIGNMENT_PROGRAM_ID != "":
                self.sys_control.generate_results_folder(self.OUTPUT_DIR_PATH)##GENERATES THE USER RESULTS FOLDER
                self.download_mode()
            else:
                self.errors.parameter_obligatory_error()

        ##IF THE USER INPUT DATA FOR DIRECTORY WITH FILES AND DONT INPUT FOR ID FILE
        elif self.INPUT_FILE_PATH == "" and self.INPUT_DIR_PATH != "":
            if self.OUTPUT_DIR_PATH != "" and self.ALIGNMENT_PROGRAM_ID != "":
                self.sys_control.generate_results_folder(self.OUTPUT_DIR_PATH)##GENERATES THE USER RESULTS FOLDER
                self.directory_mode()
            else:
                self.errors.parameter_obligatory_error()
    
    ##IT RUNS THE APLICATION, BY DOWNLOADING THE SEQUENCES
    def download_mode(self):
        ##The parameters are
        ##Source - Download -> 1
        ##ID file path
        ##output dir path
        self.mit_control.mithocondriaSource(1,self.INPUT_FILE_PATH,self.OUTPUT_DIR_PATH,self.ALIGNMENT_PROGRAM_ID)

    ##IT RUNS THE APLICATION, BY READING THE SEQUENCES INSIDE A DIRECTORY
    def directory_mode(self):
        ##The parameters are
        ##Source - Local files -> 2
        ##Directory path
        ##output dir path
        self.mit_control.mithocondriaSource(2,self.INPUT_DIR_PATH,self.OUTPUT_DIR_PATH,self.ALIGNMENT_PROGRAM_ID)
