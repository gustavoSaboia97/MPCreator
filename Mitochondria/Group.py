#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Descricao          : Control de files
# AUTOR              : Gustavo Saboia
# DATA               : 22/08/2018
#-------------------------------------------------------------------------------------

class Group:
    def __init__(self):
        self.parameters = ["rRNA            ","tRNA            ","gene            ","CDS             ","D-loop          "]
        self.rRNAs = list()
        self.tRNAs = list()
        self.genes = list()
        self.CDSs = list()
        self.D_loops = list()
        self.gb_file_data = list()
########################################################################################
    #Get the numbers of the indexes
    def indexes_translation(self,indexes_without_translate):
        indexes = []
        #For join cases
        if indexes_without_translate.count("join") > 0:
            
            indexes_string = indexes_without_translate.replace("join","")
            indexes_string = indexes_string.replace(">","")
            indexes_string = indexes_string.replace("<","")
            indexes_string = indexes_string.replace("(","")
            indexes_string = indexes_string.replace(")","")
            indexes_string_vector = indexes_string.split(",")
            
            for x in indexes_string_vector:
                simple_indexes = x.split("..")
                indexes.append(int(simple_indexes[0]))
                indexes.append(int(simple_indexes[1]))
        #For complement cases
        elif indexes_without_translate.count("complement") > 0:
            indexes_string = indexes_without_translate.replace("complement","")
            indexes_string = indexes_string.replace(">","")
            indexes_string = indexes_string.replace("<","")
            indexes_string = indexes_string.replace("(","")
            indexes_string = indexes_string.replace(")","")
            
            simple_indexes = indexes_string.split("..")
            indexes.append(int(simple_indexes[0]))
            indexes.append(int(simple_indexes[1]))
        #For normal cases
        else:
            simple_indexes = indexes_without_translate.split("..")
            indexes_string = indexes_string.replace(">","")
            indexes_string = indexes_string.replace("<","")
            indexes.append(int(simple_indexes[0]))
            indexes.append(int(simple_indexes[1]))
        return indexes
#########################################################################################
    #Insert data into the list gb variable
    def set_gbFile_list(self,parameter,indexes,name,sequence):
        base = {"group":"","index":[],"name":"","seq":""}

        if parameter.count("rRNA") > 0:
            rRNA = base.copy()
            rRNA["group"] = "rRNA"
            rRNA["index"] = indexes
            rRNA["name"] = name
            rRNA["seq"] = sequence
            self.rRNAs.append(rRNA)
        if parameter.count("tRNA") > 0:
            tRNA = base.copy()
            tRNA["group"] = "tRNA"
            tRNA["index"] = indexes
            tRNA["name"] = name
            tRNA["seq"] = sequence
            self.tRNAs.append(tRNA)
        if parameter.count("gene") > 0:
            gene = base.copy()
            gene["group"] = "gene"
            gene["index"] = indexes
            gene["name"] = name
            gene["seq"] = sequence
            self.genes.append(gene)
        if parameter.count("CDS") > 0:
            CDS = base.copy()
            CDS["group"] = "CDS"
            CDS["index"] = indexes
            CDS["name"] = name
            CDS["seq"] = sequence
            self.CDSs.append(CDS)
        if parameter.count("D-loop") > 0:
            D_loop = base.copy()
            D_loop["group"] = "D-loop"
            D_loop["index"] = indexes
            D_loop["name"] = name
            D_loop["seq"] = sequence
            self.D_loops.append(D_loop)
#########################################################################################
    #reads the sequence name and returns it
    #n_line is the position
    def get_gb_sequence_name(self,parameter,gb_file_parameter_lines,n_line):
        name = ""
        stop = False##Variable to break the loop if it start reading another group line or sequence line
        ##TO rRNA and tRNA
        if parameter.count("rRNA") > 0 or parameter.count("tRNA") > 0:
            #Range start in the next line
            for line_counter in range(n_line + 1,len(gb_file_parameter_lines)):
                ##Break the loop if the line is in another sequence
                for p in self.parameters:
                    if gb_file_parameter_lines[line_counter].count(p) > 0:
                        stop = True
                        break
                if stop:
                    break
                #GET THE NAME
                if gb_file_parameter_lines[line_counter].count("product") > 0:
                    name_vector = gb_file_parameter_lines[line_counter].split("\"")
                    name = name_vector[1]
                    break
        ##TO CDS and gene
        if parameter.count("CDS") > 0 or parameter.count("gene") > 0:
            #Range start in the next line
            for line_counter in range(n_line + 1,len(gb_file_parameter_lines)):
                ##Break the loop if the line is in another sequence
                for p in self.parameters:
                    if gb_file_parameter_lines[line_counter].count(p) > 0:
                        stop = True
                        break
                if stop:
                    break
                #GET THE NAME
                if gb_file_parameter_lines[line_counter].count("gene") > 0:
                    name_vector = gb_file_parameter_lines[line_counter].split("\"")
                    name = name_vector[1]
                    break

        if parameter.count("D-loop") > 0:
            name = "control region"
        
        return name                
#########################################################################################
    ##Get the sequences with the indexes
    def get_sequence(self,indexes_without_translate,indexes,gb_sequence):
        #Join Extraction
        sequence = ""
        if indexes_without_translate.count("join") > 0:
            for i in range(0,len(indexes)):
                if (i % 2) == 0:
                    start = indexes[i] - 1 #just because of the vector starts in zero
                    finish = indexes[i + 1] #because it alread reads 1 position before the final 
                    sequence = sequence + gb_sequence[start:finish]
                
        
        #Complement Extraction
        elif indexes_without_translate.count("complement") > 0:
            start = indexes[0] - 1 #just because of the vector starts in zero
            finish = indexes[1] #because it alread reads 1 position before the final 
            sequence = sequence + gb_sequence[start:finish]
            ##Sequence convertion
            for i in range(0,len(sequence)):
                if sequence[i] == "a":
                    sequence[i].replace("a","t")
                if sequence[i] == "A":
                    sequence[i].replace("A","T")
                if sequence[i] == "t":
                    sequence[i].replace("t","a")
                if sequence[i] == "T":
                    sequence[i].replace("T","A")
                if sequence[i] == "g":
                    sequence[i].replace("g","c")
                if sequence[i] == "G":
                    sequence[i].replace("G","C")
                if sequence[i] == "c":
                    sequence[i].replace("C","G")
                if sequence[i] == "C":
                    sequence[i].replace("T","A")

        #Normal Extraction
        else:
            start = indexes[0] - 1 #just because of the vector starts in zero
            finish = indexes[1] #because it alread reads 1 position before the final 
            sequence = sequence + gb_sequence[start:finish]

        return sequence

#########################################################################################
    #IT GETS THE PARAMETERS OF THE SEQUENCES
    def get_parameters(self,gbFile,gb_sequence):
        gb_file_parts = gbFile.split("FEATURES             Location/Qualifiers")
        gb_file_without_header = gb_file_parts[1].split("ORIGIN")
        gb_file_parameter_lines = gb_file_without_header[0].split("\n")

        
        for parameter in self.parameters:
            line_counter = 0 ##Line counter
            for i in gb_file_parameter_lines:
            #Condition to find the line with the indexes
                if i.count(parameter) > 0:
                    #Indexes identification
                    indexes_found = i.split(parameter)
                    indexes_without_translate = indexes_found[1]
                    indexes = self.indexes_translation(indexes_without_translate)##Get the numbers in order to use to get the gene sequence
                    #Name identification
                    name = self.get_gb_sequence_name(parameter,gb_file_parameter_lines,line_counter)
                    #Sequence Extraction
                    sequence = self.get_sequence(indexes_without_translate,indexes,gb_sequence)
                    #List construction
                    self.set_gbFile_list(parameter,indexes,name,sequence)

                line_counter += 1 

        ##Insert the data in the same list
        self.gb_file_data.append(self.rRNAs)
        self.gb_file_data.append(self.tRNAs)
        self.gb_file_data.append(self.genes)
        self.gb_file_data.append(self.CDSs)
        self.gb_file_data.append(self.D_loops)

        return self.gb_file_data
                    
            

#########################################################################################
        