#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Descricao          : Control de files
# AUTOR              : Gustavo Saboia
# DATA               : 22/08/2018
#-------------------------------------------------------------------------------------
from Mitochondria.Group import Group

class FileControl:
    def __init__(self):
        pass
#####################################################################################
    def getDownloadIDs(self,path):
        file_open = open(path,"r")
        file_read = file_open.read()
        file_open.close()##Close the conection with the file
        file_read_ids = file_read.split("\n")
        final_ids = list()
        for x in file_read_ids:
            if x != "":
                final_ids.append(x) 

        return final_ids
#####################################################################################
    def create_concat_file(self,seq_list,group,output_dir_path):
        complete_file = ""
        for x in seq_list:
            header = "> "+x["file"]+"\n"
            sequence = x["seq"] + "\n"
            complete_file = complete_file + header + sequence
        open(output_dir_path+"/FinalAlignment/"+group+".fasta","w").write(complete_file)
        
#####################################################################################
    ##Create the file
    def generate_file(self,gb_file_name,ouput_dir_path,group_data):
        complete_sequence_data = ""
        for x in group_data:
            header = ">  " + gb_file_name + "  |  " + x["group"] + "  |  " + x["name"] + "\n"
            complete_sequence_data = complete_sequence_data + header
            sequence = x["seq"] + "\n\n"
            complete_sequence_data = complete_sequence_data + sequence
        
        try:
            fasta_final_name = ouput_dir_path+"/"+gb_file_name+"-"+group_data[0]["group"]+".fasta"
            file_open = open(fasta_final_name,"w")
            file_open.write(complete_sequence_data)
            file_open.close()
        except IndexError:
            pass
#####################################################################################
    ##Read and returns a strutured list of sequences
    def read_aligned_files(self,names_list,output_dir_path):
        dictionary = {"file":"","group":"","name":"","seq":""}
        files_dictionary_list = list()
        ###OPEN A GROUP FILE
        for name in names_list:
            file_opened = open(name,"r").read()
            dictionary_list = list()
            ##READ the file and append it into dictionary_list
            if file_opened[0] == '>':
                continue_index = 0
                for x in range(0,len(file_opened)):
                    seq_data = dictionary.copy()
                    if file_opened[x] == '>':
                        header = ""
                        seq = ""
                        seq_index = 0
                        ##Read the header data
                        for i in range(x,len(file_opened)):
                            if file_opened[i] == '\n':
                                seq_index = i+1
                                break
                            header = header +  file_opened[i]
                        ##Read the sequence data
                        for i in range(seq_index,len(file_opened)):
                            if file_opened[i] == '>':
                                continue_index = i
                                break
                            if file_opened[i] == '\n':
                                continue
                            seq = seq +  file_opened[i]
                        ##GET THE SEQ DATA IN GENERAL
                        header = header.replace("  ","")   
                        header = header.replace(">","")      
                        header_data = header.split("|")
                        seq_data["file"] = header_data[0]
                        seq_data["group"] = header_data[1]
                        seq_data["name"] = header_data[2]
                        seq_data["seq"] = seq
                        ##PUT IT INTO A LIST
                        dictionary_list.append(seq_data)
                    x = continue_index
                    ##END OF FOR
                ##PUT IT INTO A FILES LIST
                files_dictionary_list.append(dictionary_list)
        return files_dictionary_list##RETURNS THE LIST
#####################################################################################
    ##Creates and returns the files separated by groups (rRNA,tRNA,CDS...)
    def generate_group_files(self,gb_file_name,output_dir_path,gbFile,geneSequences):
        group = Group()
        all_gbFile_data = group.get_parameters(gbFile,geneSequences)
        ##POSITIONS
        # 0 - rRNA
        # 1 - tRNA
        # 2 - gene
        # 3 - CDS
        # 4 - D-loop
        ##Create fasta files of extracted Genbank
        for x in all_gbFile_data:
            self.generate_file(gb_file_name,output_dir_path,x)

        return all_gbFile_data
#####################################################################################
    def generate_gene_files(self,gb_file_name,gb_file_extracted,output_dir_path):
        for group in gb_file_extracted:
            for gene in group:
                ##Sequence caracteristics
                fasta_file = ">  " + gb_file_name + "  |  " + gene["group"] + "  |  " + gene["name"] + "\n"
                fasta_file = fasta_file + gene["seq"] + "\n"

                ##File caracteristics
                fasta_file_name = output_dir_path+"/toAlign/"+gene["name"].replace(" ","_")+"-"+gene["group"]+".fasta"
                fasta_gene_file = open(fasta_file_name,"a")
                fasta_gene_file.write(fasta_file)
                fasta_gene_file.close()
                
            
                   
