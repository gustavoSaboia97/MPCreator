#! /usr/bin/env python
# -*- coding: utf-8 -*-
# TITULO             : Muscle: Alinhamento de sequencias
# AUTOR              : Gustavo Saboia
# DATA               : 26/10/2017
#-------------------------------------------------------------------------------------
##Classe de Controle do Programa Muscle
import subprocess;
from ControleArquivo import ControleArquivo;
class Muscle:
	
	def __init__(self):
		self.home = subprocess.getoutput("echo $HOME");
		self.outDir = self.home+"/MPResults/";

	##Função de Alinhamento com o Muscle
	def alinhar(self,arquivo,dirName):
		#Cria um diretório para os resuldados do Programa
		split1 = arquivo.split("/");
		split2 = split1[-1].split(".fasta");
		fileName = split2[0];

		self.outDir = self.outDir + dirName + "/Alignment/";

		term = "muscle -in "+arquivo+" -out "+self.outDir+fileName+".fasta";
		muscleOutput = subprocess.getoutput(term);
		controleArquivo = ControleArquivo();
		resposta = controleArquivo.verificarConclusao(self.outDir,fileName,".fasta");
		
		if resposta:
			return True;
		else:
			return False;
