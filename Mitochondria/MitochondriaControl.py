#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Descricao          : Start the Mithocondria Modules
# AUTOR              : Gustavo Saboia
# DATA               : 22/08/2018
#-------------------------------------------------------------------------------------
from Mitochondria.FileControl import FileControl
from Alignment.Alignment import Alignment
from Classes.Errors import Errors
from Classes.Interface import Interface
from Classes.SystemControl import SystemControl
import subprocess,os

class MitochondriaControl:
    def __init__(self):
        self.ALIGNMENT_PROGRAM_ID = str()
        self.gbFiles = list()
        self.gb_files_names = list()
        self.geneSequencies = list()
        self.all_extracted_files = list()
        self.continueFlow = bool
        self.errors = Errors()
        self.interface = Interface()
        self.sys_control = SystemControl()
    
###########################################################################
    def genbankSequenceExtraction(self,gbFile,gbFileName):
		##Control the files
        situation = False
        ##Verifies if there is a sequence ORIGIN
        if gbFile.count("ORIGIN") > 0:
            gbFile_split = gbFile.split("ORIGIN")
            gbFile_seq_extract = gbFile_split[1]
            gbFile_seq_extract = gbFile_seq_extract.replace("//","")
			#remove the numbers
            for x in range(0,len(gbFile_seq_extract)):
                gbFile_seq_extract = gbFile_seq_extract.replace(str(x),"")
			##Separates into only the gene sequence
            gbFile_seq_extract = gbFile_seq_extract.replace(" ","")
            gbFile_seq_extract = gbFile_seq_extract.replace("\n","")
			
            situation = True
            self.interface.genbank_extraction_outputs(False,gbFileName,situation)###Just to indicate the reading status
        else:
            self.continueFlow = False	
            self.interface.genbank_extraction_outputs(False,gbFileName,situation)###Just to indicate the reading status

        if situation:
            self.gbFiles.append(gbFile)
            self.geneSequencies.append(gbFile_seq_extract)
#################################################################################################
## RESPONSABLE FOR MAKE THE DIFFERENCIATION ABOUT THE SAME NAMES IN SEQUENCES OF THE SAME FILE ##
#################################################################################################
    def verify_sequence_names(self):
        ##Get the extracted file
        for gb_file_extracted in self.all_extracted_files:
            ##Get the Gene group
            for group in gb_file_extracted:
                for gene in group:
                    i = 2
                    for gene2 in group:
                        if gene == gene2:
                            continue
                        if gene["name"] == gene2["name"]:
                            gene2["name"] = gene2["name"]+str(i)
                            i += 1
###########################################################################
## PREPARE THE DATA FOR MULTIPLE ALIGNMENT ################################
###########################################################################
    def prepareToAlignment(self,output_dir_path):
        fileControl = FileControl()
        i = 0
        for x in self.gbFiles:
            ##Get the extracted files into a list with separated data
            self.all_extracted_files.append(fileControl.generate_group_files(self.gb_files_names[i],output_dir_path,x,self.geneSequencies[i]))
            i += 1
        ##Organize the names to create the files
        self.verify_sequence_names()
        ###Creates the files
        i = 0
        for x in self.all_extracted_files:
            fileControl.generate_gene_files(self.gb_files_names[i],x,output_dir_path)
            i += 1

###########################################################################
## DO THE ALIGNMENT #######################################################
###########################################################################
    def do_aligment(self,output_dir_path):
        terminal_string = "ls "+output_dir_path+"/toAlign"
        names_list = subprocess.getoutput(terminal_string)

        files_list = names_list.split("\n")
        
        alignment = Alignment()
        alignment.executeMultipleAlignments(files_list,output_dir_path,self.ALIGNMENT_PROGRAM_ID)
###########################################################################
## DO THE CONCATENATION ###################################################
###########################################################################
    def concat(self,group,output_dir_path):
        dictionary = {"file":"","group":"","name":"","seq":""}
        concat_dictionary = {"file":"","seq":""}
        concat_dictionary_list = list()

        fileControl = FileControl()
        ###GROUP
        terminal_string = "ls "+output_dir_path+"/Alignment/*-"+group+".fasta"
        names_list = subprocess.getoutput(terminal_string)
        files_list = names_list.split("\n")

        group_list = fileControl.read_aligned_files(files_list,output_dir_path)
        ####FOR TO VERIFY IF A FILE CONTAINS THE SAME SEQUENCES, IF NOT PUT A GAP ON IT
        for fasta in group_list:
            for name in self.gb_files_names:
                exists = False
                ##Verify if there is a sequence of that ID inside de alignment
                for seq in fasta:
                    if seq["file"] == name:
                        exists = True
                        break
                if exists == False:
                    n_gaps = len(fasta[0]["seq"])
                    seq_gaps = ""
                    for i in range(0,n_gaps):
                        seq_gaps = seq_gaps + "-"

                    data = dictionary.copy()
                    data["file"] = name
                    data["group"] = fasta[0]["group"]
                    data["name"] = fasta[0]["name"]
                    data["seq"] = seq_gaps
                    fasta.append(data.copy())
        ##END FOR

        ###Get the files names
        for name in self.gb_files_names:
            data = concat_dictionary.copy()
            data["file"] = name
            concat_dictionary_list.append(data.copy())
        ###CONCAT
        for fasta in group_list:
            for file_dic in concat_dictionary_list:
                for seq in fasta:
                    if seq["file"] == file_dic["file"]:
                        file_dic["seq"] = file_dic["seq"] + seq["seq"]
        ##WRITE A FILE   
        fileControl.create_concat_file(concat_dictionary_list,group,output_dir_path)    

###########################################################################
## DO THE CONCATENATION ###################################################
###########################################################################
    def do_concatenation(self,output_dir_path):
        self.concat("tRNA",output_dir_path)
        self.concat("rRNA",output_dir_path)
        self.concat("gene",output_dir_path)
        self.concat("CDS",output_dir_path)
        self.concat("D-loop",output_dir_path)

        



#############################################################################
############# DOWNLOAD METHOD ###############################################
#############################################################################
    def downloadMethod(self,path,output_dir_path):
        fileControl = FileControl()
        ids = fileControl.getDownloadIDs(path)
        self.interface.genbank_extraction_outputs(True,"",False)###Just to indicate that you're downloading
        if len(ids) > 1:
            for id in ids:
                self.gb_files_names.append(id)##Save the ids into a variable
                terminal_string = "efetch -db nucleotide -id "+id+" -format gb"
                gbfile = subprocess.getoutput(terminal_string)
                self.genbankSequenceExtraction(gbfile,id)
                if self.continueFlow == False:
                    self.errors.download_error()
                    break
            ##Creates gb files inside a genbank folder, just to save it
            self.sys_control.generate_gb_folder(output_dir_path)
            self.sys_control.create_gb_files(ids,self.gbFiles,output_dir_path)
            self.prepareToAlignment(output_dir_path)#Divides the files into small files with similar sequences
            self.do_aligment(output_dir_path)
            self.do_concatenation(output_dir_path)
        else:
            self.errors.file_quantity_error()
#############################################################################
#############################################################################
############## LOCAL FILES METHOD ###########################################
#############################################################################
    def localFilesMethod(self,dir_path,output_dir_path):
        abs_dir_path = os.path.abspath(dir_path)
        ##Get the names of the files inside a vector
        terminal_string = "ls "+abs_dir_path
        files = subprocess.getoutput(terminal_string)
        gb_files_names = files.split("\n")
        self.gb_files_names = gb_files_names##Save the names into a variable
        if len(gb_files_names) > 1:
            ##Load every Genbank file
            for gb_file_name in gb_files_names:
                if gb_file_name != "":
                    gb_file_opened = open(abs_dir_path+"/"+gb_file_name,"r")
                    gb_file = gb_file_opened.read()
                    self.genbankSequenceExtraction(gb_file,gb_file_name)
                    if self.continueFlow == False:
                        self.errors.reading_error()
                        break
            ##Creates gb files inside a genbank folder, just to save it
            self.prepareToAlignment(output_dir_path)#Divides the files into small files with similar sequences
            self.do_aligment(output_dir_path)
            self.do_concatenation(output_dir_path)
        else:
            self.errors.file_quantity_error()
#############################################################################
    # 1 - Download
    # 2 - Local directory
    # Path can be a directory or a file with ids
    def mithocondriaSource(self,source_id,input_path,output_dir_path,ALIGNMENT_PROGRAM_ID):
        self.ALIGNMENT_PROGRAM_ID = ALIGNMENT_PROGRAM_ID
        ##Download Method
        if source_id == 1:
            self.downloadMethod(input_path,output_dir_path)
        ##Local Files Method
        if source_id == 2:
            #Local directory
            self.localFilesMethod(input_path,output_dir_path)