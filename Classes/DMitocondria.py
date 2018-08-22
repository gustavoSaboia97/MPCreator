#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Descricao          : Fazer o Download dos arquivos fasta no site NCBI concatenando por grupos
# AUTOR              : Gustavo Saboia
# DATA               : 16/12/2017
#-------------------------------------------------------------------------------------
from ControleArquivo import ControleArquivo
from Alinhamento import Alinhamento
import subprocess

class DMitocondria:
	def __init__(self):
		self.downloadsFeitos = list()
		self.listaCaminhos = ""
		self.arquivosFasta = list()
		self.arquivoGB = list()
		self.sequencias = list()
		self.caminho = str()
		self.continuar = True
		self.dirName = str()

	def criarPastaResultados(self):
		##Função para criar pasta de resultados finais
		print("Please put a name to the output folder")
		nome = input("Output Folder: ")
		self.dirName = nome
		controleArquivo = ControleArquivo()
		self.caminho = controleArquivo.pastaMitocondria(nome)

	def returnDirName(self):
		return self.dirName
		
	def retornarCaminho(self):
		return self.caminho

	##Faz o download de uma sequencia do banco NCBI
	def download(self,db,idSequencia):
		termSequencia = "efetch -db "+db+" -id "+idSequencia+" -format fasta"
		termGB = "efetch -db "+db+" -id "+idSequencia+" -format gb"
		##Baixar 2 sequencias a gb e a fasta(Pois é mais facil obter a sequencia da fasta).
		fastaFile = subprocess.getoutput(termSequencia)
		gbFile = subprocess.getoutput(termGB)
		sequenciaGen = str()
		stringSeq = ""
		if (fastaFile[0] == ">"):##Comprova se o arquivo é real
			i = 0
			j = 0
			chave = 0
			##ler somente a sequencia genética
			for i in range(len(fastaFile)):
				if (fastaFile[i] == ">"):
					for j in range(len(fastaFile)):
						if (fastaFile[j] == "\n"):
							chave = j + 1
							break
					break
			for i in range(chave,len(fastaFile)):
				if (fastaFile[i] != "\n"):
					stringSeq =  stringSeq + str(fastaFile[i])

			

			string = " -> DONE"
			situacao = True
		else: 
			string = " -> ERROR!!"
			situacao = False
			self.continuar = False


		print (idSequencia+string)
		self.downloadsFeitos.append(situacao)
		if (situacao):
			self.arquivoGB.append(gbFile)
			self.sequencias.append(stringSeq);	

	def controlarSequencias(self,db,vetorSequencia):
		for id in vetorSequencia:
			if id == "":
				continue
				
			self.download(db,id)

	##Função de criar um arquivo genes de uma mitocondria
	def gerarArquivoDataset(self,vetorSequencia):
		for i in range(0,len(self.downloadsFeitos)):
			if (self.downloadsFeitos[i] == True):	
				self.criarPastaResultados()
				break

		for arqs in range(0,len(self.arquivoGB)):
			##Verifica se há nos arquivos as divisões antes de realizar
			if (self.arquivoGB[arqs].count("tRNA            ")>= 0):
				self.separarBases("tRNA            ", "tRNA",arqs,vetorSequencia)
			if (self.arquivoGB[arqs].count("rRNA            ")>= 0):
				self.separarBases("rRNA            ", "rRNA",arqs,vetorSequencia)
			#if (self.arquivoGB[arqs].count("gene            ")>= 0):
			#	self.separarBases("gene            ", "gene",arqs,vetorSequencia)			
			if (self.arquivoGB[arqs].count("CDS             ")>= 0):	
				self.separarBases("CDS             ", "CDS",arqs,vetorSequencia)
			if (self.arquivoGB[arqs].count("D-loop          ")>= 0):#Bloqueado pois possui somente uma sequencia
				self.separarBases("D-loop          ", "D-loop",arqs,vetorSequencia)
	
	def separarAlinhamentos(self):
		controle = ControleArquivo()
		count = 1

		self.listaCaminhos = self.listaCaminhos + controle.prepararParaAlinhamento("rRNA",self.caminho,count)
		self.listaCaminhos = self.listaCaminhos + controle.prepararParaAlinhamento("tRNA",self.caminho,count)
		self.listaCaminhos = self.listaCaminhos + controle.prepararParaAlinhamento("CDS",self.caminho,count)
		#self.listaCaminhos = self.listaCaminhos + controle.prepararParaAlinhamento("gene",self.caminho,count)
		self.listaCaminhos = self.listaCaminhos + controle.prepararParaAlinhamento("D-loop",self.caminho,count)


	def separarBases(self,stringSplit, tipoS, arq, vetorSequencia):
		tipo = self.arquivoGB[arq].split(stringSplit)
		indicesTipo = list()
		nomesTipo = list()
		arquivoFasta = ""
		if ( len(tipo) != 1 ):##Caso nao exista a string do split
			for i in range(1,len(tipo)):##A partir do primeiro pois a posição 0 é cabeçalho
				num = tipo[i].split("\n")
				if (tipoS == "D-loop"):
					nome = list()
					nome.append("0")
					nome.append("control region")
				elif (tipoS == "tRNA"):
					for x in range(0,len(num)):
						if (num[x].count("product") == 1):
							nome = num[x].split("\"")
							break

				else:
					nome = tipo[i].split("\"")


				indicesTipo.append(num[0]);##Posição 0 pois é antes do split
				nomesTipo.append(nome[1]);##Posição 1 logo após as aspas
			##Resolver questao de nomes iguais
			for i in range (0,len(nomesTipo)):
				cont = 1
				if (i != (len(nomesTipo) - 1)):
					for j in range(i+1, len(nomesTipo)):
						if (nomesTipo[i] == nomesTipo[j]):
							nomesTipo[j] = nomesTipo[j] + str(cont)
							cont += 1

			for i in range(0,len(nomesTipo)):
				stringSequencia = ">"+vetorSequencia[arq]+"|"+str(nomesTipo[i])+"|"+tipoS+"\n";##Cabeçalho Fasta
				veracidade = False
				if (indicesTipo[i].count("complement(") >= 1):
					stringInd = indicesTipo[i].split("complement(")
					stringFinal = stringInd[1].split(")")
					indices = stringFinal[0].split("..")
					veracidade = True
				
				elif(indicesTipo[i].count("join(")):
					stringInd = indicesTipo[i].split("join(")
					string4indices = stringInd[1].split(")")
					stringFinais = string4indices[0].split(",")
					indices = stringFinais[0].split("..")
					indices2 = stringFinais[1].split("..")
				else:
					indices = indicesTipo[i].split("..")

				for x in range (0,len(indices)):
					if (indices[x].count(">") >= 1):
						indices[x] = indices[x].replace(">","")
					if (indices[x].count("<") >= 1):
						indices[x] = indices[x].replace("<","")
				
				sequencia = self.sequencias[arq];		
				if (veracidade):
					sequencia2 = sequencia[int(indices[0]):int(indices[1])]
					sequencia2C = ""
					for x in range(0,len(sequencia2)):
						if (sequencia2[x] == "A"):
							sequencia2C = sequencia2C + "T"
							continue;
						if (sequencia2[x] == "T"):
							sequencia2C = sequencia2C + "A"
							continue;
						if (sequencia2[x] == "G"):
							sequencia2C = sequencia2C + "C"
							continue;
						if (sequencia2[x] == "C"):
							sequencia2C = sequencia2C + "G"
							continue

					sequencia3 = ""

					for gene in sequencia2C:
						sequencia3 = gene + sequencia3

					stringSequencia = stringSequencia+sequencia3
				else:
					stringSequencia = stringSequencia+sequencia[int(indices[0])-1:int(indices[1])]
				
					if (indicesTipo[i].count("join(")):
						stringSequencia = stringSequencia + sequencia[int(indices2[0]):int(indices2[1])]

				arquivoFasta = arquivoFasta +stringSequencia+"\n"
			controleArquivo = ControleArquivo();	
			caminho = controleArquivo.criarArquivoDownloadM(self.caminho,vetorSequencia[arq]+"-"+tipoS,arquivoFasta)



	def executar(self,db,vetorSequencia): 
		print("---Download Mitocondrial---")
		self.controlarSequencias(db,vetorSequencia)
		self.gerarArquivoDataset(vetorSequencia)
		
		if (self.continuar):
			self.separarAlinhamentos()
			return self.listaCaminhos

		print("ERROR: The Sequences were not downloaded")
		return None