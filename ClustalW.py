#! /usr/bin/env python
# -*- coding: utf-8 -*-
# TITULO             : ClustalW: Alinhamento de sequencias
# AUTOR              : Gustavo Saboia
# DATA               : 07/11/2017
#-------------------------------------------------------------------------------------
import os, subprocess;
from ControleArquivo import ControleArquivo;
class ClustalW:
	def __init__(self):
		self.home = subprocess.getoutput("echo $HOME");
		self.outDir = self.home+"/MPResults/";

	def alinhar(self,arquivo, dirName):
		split1 = arquivo.split("/");
		split2 = split1[-1].split(".fasta");
		fileName = split2[0];

		self.outDir = self.outDir + dirName + "/Alignment/";

		term = "clustalw -infile="+arquivo+" -align -OUTFILE="+self.outDir+fileName+".fasta -OUTPUT=FASTA";
		os.chdir("/");##Clustal necessita de arquivos em diretorios presentes ou subdiretorios
		saidaClustal = subprocess.getoutput(term);
		controleArquivo = ControleArquivo();
		resposta = controleArquivo.verificarConclusao(self.outDir,fileName,".fasta");

		if resposta:
			return True;
		else:
			return False;
