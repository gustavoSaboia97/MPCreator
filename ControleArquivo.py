#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Descricao          : Arquivo de Controle de Arquivos
# AUTOR              : Gustavo Saboia
# DATA               : 27/10/2017
#-------------------------------------------------------------------------------------
#Classe de controle de arquivos a níveis gerais, sem especificações
import os, sys, subprocess,shutil;


class ControleArquivo:	
	###Método Construtor	
	def __init__(self):
		pass

	def prepararParaAlinhamento(self,stringTipo,dirPadrao,count):
		saidaTerm = subprocess.getoutput("ls "+dirPadrao+"/*-"+stringTipo+"*.fasta");
		arquivos = saidaTerm.split("\n");
		listaCaminhos = "";


		for arq in range (0,len(arquivos)):
			fileOpen = open(arquivos[arq],"r");
			arquivo = fileOpen.read();
			pontoInicial = 0;
			if (arquivo[0] == ">"):
				for i in range(0,len(arquivo)):
					cabecario = "";
					sequencia = "";
					
					if (arquivo[i] == ">"):
						for x in range(pontoInicial,len(arquivo)):
							cabecario = cabecario + arquivo[x];
							if (arquivo[x] == "\n"):
								pontoInicial = x+1;
								break;
						
						for x in range(pontoInicial,len(arquivo)):
							if (arquivo[x] == ">"):
								pontoInicial = x;
								i = x - 1;
								break;
							sequencia = sequencia + arquivo[x];
						
						arquivoFasta = cabecario + sequencia;
						nomeSplit = cabecario.split("|");
						nomeSplit2 = nomeSplit[2].split("\n");
						nomeNovoArquivo = nomeSplit[1].split(" ");
						novoArquivo = open(dirPadrao+"/toAlign/"+str(count)+"-"+nomeNovoArquivo[0]+nomeSplit2[0]+".fasta","a");
						novoArquivo.write(arquivoFasta);			
						listaCaminhos = listaCaminhos + dirPadrao+"/toAlign/"+str(count)+"-"+nomeNovoArquivo[0]+nomeSplit2[0]+".fasta" + ",";
		return listaCaminhos;

	def concatenarMitocondria(self,dirAlinhamento,tipoGene):
		saida = subprocess.getoutput("ls "+dirAlinhamento+"/Alignment/*"+tipoGene+"*.fasta");
		arquivos = saida.split("\n");

		arquivoFasta = "";
		sequencia = "";
		nomeArquivoFinal = tipoGene+".fasta";

		pontoInicial = list();
		for x in range(0, len(arquivos)):
			pontoInicial.append(0);

		#Preecher Repetiçao
		repeticao = list();
		for x in range(0, len(arquivos)):
			files = open(arquivos[x],"r");
			leitura = files.read();
			repeticao.append(leitura.count(">"));

		#decobrir o menor indice
		menor = repeticao[0];
		for x in range (0, len(arquivos)):
			if (menor > repeticao[x]):
				menor = repeticao[x];

		contador = 1;
		while (contador <= menor):
			cabecarioFinal = "";
			sequenciaFinal = "";
			arquivoFasta = "";
			for arq in range(0,len(arquivos)):
				fopen = open(arquivos[arq],"r");
				arquivo = fopen.read();
				sequencia = "";
			

				if (arquivo[0] == ">"):
					cabProvisorio = "";
					key = 0;
					for x in range(pontoInicial[arq],len(arquivo)):
						if (arquivo[x] == "\n"):
							key = x + 1;
							break;
						cabProvisorio = cabProvisorio + arquivo[x];
					cabSplit = cabProvisorio.split("|");
					cabecario = cabSplit[0]+"|"+cabSplit[2]+"\n";
					if (arq == 0):
						if (cabecarioFinal == ""):
							cabecarioFinal = cabecario;

					if (cabecarioFinal == cabecario):
						for x in range (key,len(arquivo)):
							if (arquivo[x] == ">"):
								pontoInicial[arq] = x;
								break;
							if (arquivo[x] != "\n"):
								sequencia = sequencia + arquivo[x];
					sequenciaFinal = sequenciaFinal + sequencia;
			geneCompleto = cabecarioFinal + sequenciaFinal + "\n";
			arquivoFasta = arquivoFasta + geneCompleto;
			nomePasta = dirAlinhamento.split("/");
			arquivoFinal = open(dirAlinhamento+"/FinalAlignment/"+nomePasta[-1]+nomeArquivoFinal,"a");
			arquivoFinal.write(arquivoFasta);
			arquivoFinal.close();
			contador += 1;

	def pastaMitocondria(self,nome):
		saidaTerm = subprocess.getoutput("mkdir ~/MPResults/"+nome);
		##Pasta com os arquivos alinhados separadamente
		saidaTerm = subprocess.getoutput("mkdir ~/MPResults/"+nome+"/Alignment");
		##Pasta com os arquivos finais alinhados
		saidaTerm = subprocess.getoutput("mkdir ~/MPResults/"+nome+"/FinalAlignment");
		##Pasta dos arquivos a serem alinhados
		saidaTerm = subprocess.getoutput("mkdir ~/MPResults/"+nome+"/toAlign");
		home = subprocess.getoutput("echo $HOME");
		caminhoPasta = home + "/MPResults/"+nome;
		return caminhoPasta;

	##Diretórios dos Downloads do site NCBI
	def criarDirResultados(self):
		saidaTerm = subprocess.getoutput("mkdir ~/MPResults");
		print("---------------------------------------");

	def criarArquivoDownloadM(self,caminho,nomeArquivo,fastaFile):
		home = subprocess.getoutput("echo $HOME");
		arquivo = caminho+"/"+nomeArquivo+".fasta";			
		fileOpen = open(arquivo,"w");
		fileOpen.write(fastaFile+"\n");
		fileOpen.close();
		return arquivo;
	
	def arquivoSaida(self,arquivoSaida,saidaPrograma):
		fileOpen = open(arquivoSaida,"w");
		fileOpen.write(saidaPrograma);
		fileOpen.close();

	##Método de Verificação de existência de saida
	def verificarConclusao(self,caminhoPrograma,nomeArquivo,extencao):
		existe = os.path.isfile(caminhoPrograma+nomeArquivo+extencao);
		if existe:
			tamanho = os.path.getsize(caminhoPrograma+nomeArquivo+extencao);
			if tamanho == 0:
				return False;
		else:
			return False;
		return True;


	##Função de verificar a existência do arquivo
	def verificarLocalArquivo(self, caminho):
		return os.path.isfile(caminho);

	def verificarPrograma(self, programa):
		saida = subprocess.getoutput("dpkg -l | grep "+programa);
		if len(saida) != 0:
			return True;
		return False;

