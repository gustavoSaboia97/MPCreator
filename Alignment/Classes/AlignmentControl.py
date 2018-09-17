#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Descricao          : Control the alignment flow
# AUTOR              : Gustavo Saboia
# DATA               : 22/08/2018
#-------------------------------------------------------------------------------------
from Alignment.Alignment_Classes.Muscle import Muscle
from Alignment.Alignment_Classes.Mafft import Mafft
from Alignment.Alignment_Classes.T_Coffee import T_Coffee

class AlignmentControl:
    def __init__(self):
        pass

    def alignmentProgramDecision(self,input_file_path,output_dir_path,program_id):
        if program_id == "1":
            mafft = Mafft()
            done = mafft.align(input_file_path,output_dir_path)
            del mafft
            return done
        if program_id == "2":
            muscle = Muscle()
            done = muscle.align(input_file_path,output_dir_path)
            del muscle
            return done
        if program_id == "3":
            t_coffee = T_Coffee()
            done = t_coffee.align(input_file_path,output_dir_path)
            del t_coffee
            return done

    def multipleAlignmentProgramDecision(self,input_file_paths,output_dir_path,program_id):
        if program_id == "1":
            mafft = Mafft()
            done = list()
            
            for input_file in input_file_paths:
                done.append(mafft.align(input_file,output_dir_path))

            del mafft
            return done
        if program_id == "2":
            muscle = Muscle()
            done = list()
            
            for input_file in input_file_paths:
                done.append(muscle.align(input_file,output_dir_path))

            del muscle
            return done
        if program_id == "3":
            t_coffee = T_Coffee()
            done = list()
            
            for input_file in input_file_paths:
                done.append(t_coffee.align(input_file,output_dir_path))

            del t_coffee
            return done

    # 1 - Mafft
    # 2 - Muscle
    # 3 - ClustalW
    # 4 - T_Coffee
    def executeMultipleAlignments(self,input_file_paths,output_dir_path,program_id):
        return self.multipleAlignmentProgramDecision(input_file_paths,output_dir_path,program_id)

    # 1 - Mafft
    # 2 - Muscle
    # 3 - ClustalW
    # 4 - T_Coffee
    def executeSingleAlignment(self,input_file_path,output_dir_path,program_id):
        return self.alignmentProgramDecision(input_file_path,output_dir_path,program_id)
        

        
