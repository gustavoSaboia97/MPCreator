#! /usr/bin/env python
# -*- coding: utf-8 -*-
# TITULO             : Mafft: Alinhamento de sequencias
# AUTOR              : Gustavo Saboia
# DATA               : 26/10/2017
#-------------------------------------------------------------------------------------
import os, subprocess, string;
from ControleArquivo import ControleArquivo;

class Mafft:

	def __init__(self):
		self.home = subprocess.getoutput("echo $HOME");
		self.outDir = self.home+"/MPResults/";

	##Conta o número de sequencias dentro do arquivo de entrada padrão Fasta.
	def contarSequencias(self,arquivo):
		try:
			text = open(arquivo).read();
			return text.count('>');
		except FileNotFoundError:
			print(arquivo); 

	##Decide a melhor linha de comando para o arquivo no MAFFT
	def definirLinhaComando(self, arquivo,fileName):
		if self.numeroSequencias < 200:
			term = "mafft --localpair --maxiterate 1000 "+arquivo+" > "+self.outDir+fileName+".fasta" ;
			
		elif self.numeroSequencias > 2000:	
			term = "mafft --retree 1 --maxiterate 0 "+arquivo+" > "+self.outDir+fileName+".fasta";
		else:
			term = "mafft --retree 2 --maxiterate 1000 "+arquivo+" > "+self.outDir+fileName+".fasta";

		mafftOutput = subprocess.getoutput(term);	
		del mafftOutput;

	##Método principal da classe Mafft para Alinhamento
	##Variável arquivo é o caminho do arquivo de entrada
	##Variável tipoAlinhamento é se é Nucleotídeo ou Aminoácido
	def alinhar(self,arquivo,dirName):
		split1 = arquivo.split("/");
		split2 = split1[-1].split(".fasta");
		fileName = split2[0];


		self.outDir = self.outDir + dirName + "/Alignment/";


		controleArquivo = ControleArquivo();
		self.numeroSequencias = self.contarSequencias(arquivo);

		self.definirLinhaComando(arquivo,fileName);


		resposta = controleArquivo.verificarConclusao(self.outDir,fileName,".fasta");
		
		
		if resposta:
			return True;
		else:
			return False;
		
	


