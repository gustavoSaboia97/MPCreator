#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Descricao          : Start the Alignment Modules
# AUTOR              : Gustavo Saboia
# DATA               : 22/08/2018
#-------------------------------------------------------------------------------------
from Alignment.Classes.AlignmentControl import AlignmentControl
import sys

class Alignment:
    def __init__(self):
        pass

    def executeSingleAlignment(self,input_file_path,output_dir_path,program_id):
        alignmentControl = AlignmentControl()
        alignmentControl.executeSingleAlignment(input_file_path,output_dir_path,program_id)

    def executeMultipleAlignments(self,input_file_paths,output_dir_path,program_id):
        alignmentControl = AlignmentControl()
        alignmentControl.executeMultipleAlignments(input_file_paths,output_dir_path,program_id)
