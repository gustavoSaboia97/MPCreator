#! /usr/bin/env python
# -*- coding: utf-8 -*-
# TITULO             : TCoffee: Alinhamento de sequencias
# AUTOR              : Gustavo Saboia
# DATA               : 26/10/2017
#-------------------------------------------------------------------------------------
import subprocess,os;
from ControleArquivo import ControleArquivo;

class T_Coffee:
	def __init__(self):
		self.home = subprocess.getoutput("echo $HOME");
		self.outDir = self.home+"/MPResults/";

	def alinhar(self,arquivo,dirName):

		split1 = arquivo.split("/");
		split2 = split1[-1].split(".fasta");
		fileName = split2[0];

		self.outDir = self.outDir + dirName + "/Alignment/";

		os.chdir(self.outDir);##redirecionar o arquivo .dnd
		arquivoSaida = self.outDir+fileName+".fasta";
		term = "t_coffee -in "+arquivo+ " -outfile "+arquivoSaida+" -output fasta_aln";
		tOut = subprocess.getoutput(term);
		
		controleArquivo = ControleArquivo();
		resposta = controleArquivo.verificarConclusao(self.outDir,fileName,".fasta");
		if resposta:
			return True;
		else:
			return False;
