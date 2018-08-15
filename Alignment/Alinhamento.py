#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Descricao          : Escolha e Execução de programas de alinhamento
# AUTOR              : Gustavo Saboia
# DATA               : 09/11/2017
#-------------------------------------------------------------------------------------
#Programa de gerenciamento de workflows para filogenia
from ControleArquivo import ControleArquivo;
from Mafft import Mafft;
from Muscle import Muscle;
from ClustalW import ClustalW;
from T_Coffee import T_Coffee;
class Alinhamento:	
	def __init__(self):
		self.escolha = 0;
		self.caminho = "";
	
	def menu(self):
		print("\nAlignment Programs:");

		##variavél para verificar se todos os programas existem
		lista_programas = list();
		n_programas = 0;

		controleArquivo = ControleArquivo();

		##While de validação da escolha de Alinhamento
		while(True):
			if controleArquivo.verificarPrograma("mafft"):
				print("1 --> Mafft");
				lista_programas.append(1);
				n_programas+=1;
			else:
				print("1 --> Mafft :: NOT DETECTED");
			if controleArquivo.verificarPrograma("muscle"):
				print("2 --> Muscle");
				lista_programas.append(2);
				n_programas+=1;
			else:
				print("2 --> Muscle :: NOT DETECTED");
			if controleArquivo.verificarPrograma("clustalw"):
				print("3 --> ClustalW");
				lista_programas.append(3);
				n_programas+=1;
			else:
				print("3 --> ClustalW :: NOT DETECTED");
			if controleArquivo.verificarPrograma("t-coffee"):
				print("4 --> T_Coffee");
				lista_programas.append(4);
				n_programas+=1;			
			else:
				print("4 --> T_Coffee :: NOT DETECTED");
			
			if n_programas == 0:
				print("This program can't continue because you don't have any alignment program");
				exit();
			
			## Caso seja digitado letras e não números
			try :
				if len(lista_programas) == 1:
					escolha  = lista_programas[0];
				else:			
					escolha = int(input("Op: "));
			
				if (escolha == 1 or escolha == 2 or escolha == 3 or escolha == 4 ):
					self.escolha = escolha;
					return escolha;
				else:
					print("Invalid Choice!!");

			except (TypeError,ValueError,NameError):
				print("Invalid Character!");
		print ("-------------------------------------------------------");

	##Metodo que chama as classes de alinhamento
	def escolhaAlinhamento(self,escolha,arquivo,dirName):
		##MAFFT		
		if (escolha == 1):
			mafft = Mafft();
			rs = mafft.alinhar(arquivo,dirName);
			return rs;##Variavel com a veracidade de resultado do MAFFT;
		##MUSCLE
		if (escolha == 2):
			muscle = Muscle();
			rs = muscle.alinhar(arquivo,dirName);
			return rs;##Variavel com a veracidade de resultado do Muscle;
		##ClustalW
		if (escolha == 3):
			clustal = ClustalW();
			rs = clustal.alinhar(arquivo, dirName);
			return rs;##Variavel com a veracidade de resultado do ClustalW;	
		##TCOFFEE
		if (escolha == 4):
			tcoffee = T_Coffee();
			rs = tcoffee.alinhar(arquivo,dirName);
			return rs;
		##if (escolha == 10):
		##	mafft = Mafft();
		##	muscle = Muscle();

		##	thread1 = Thread(target = mafft.alinhar, args = (arquivo,));
		##	thread2 = Thread(target = muscle.alinhar, args = (arquivo,));
		##	thread1.start();
		##	thread2.start();
		##	thread1.join();
		##	thread2.join();
	def retornarEscolha(self):
		return self.escolha;

	def obterArquivoAlinhado(self,arquivo):
		controle = ControleArquivo();
		if(self.escolha == 1):
		 	self.caminho = controle.obterArquivoAlinhado(arquivo,"Mafft");
		if(self.escolha == 2):
			self.caminho = controle.obterArquivoAlinhado(arquivo,"Muscle");
		if(self.escolha == 3):
		 	self.caminho = controle.obterArquivoAlinhado(arquivo,"ClustalW");
		if(self.escolha == 4):
			self.caminho = controle.obterArquivoAlinhado(arquivo,"T_Coffee");
		return self.caminho;

	def alinhar(self,arquivo,tipoAlinhamento):		
		return self.alinharSequencias(arquivo,tipoAlinhamento);
		
		
