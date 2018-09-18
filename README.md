# MPCreator
MPCreator is a scientific workflow to control and automate the treatment of genomic metadata for phylogenomics analyses. 
## Location
MPCreator is available at: https://github.com/gustavoSaboia97/MPCreator .

## Docker
This repository contains a dockerfile with the dependecies inside the folder Dockerfile. If you want to run that application inside the docker container you should follow the next terminal commands.  
```
   # cd Dockerfile/
   # docker build -t mpcreator .
   # docker run -it mpcreator /bin/bash
```

## Aplication Details
If you don't want to run that application inside a Docker container, you should know the dependencies before running the application.

### Dependencies

* Python3 
* NCBI E-Direct;
* Mafft
* Muscle
* T-Coffee

If you are using 'apt-get' as your packages manager, to install the dependencies you can use the following terminal command:
```
    $  apt-get update \
       && apt-get install -y nano git \
       && apt-get install -y python3 mafft muscle t-coffee ncbi-entrez-direct
```
### Running the Application
If you want to run the application, you must choose between two options, you can execute by downloading the sequences from NCBI database or you can execute it using a local directory with mitochondrial genbank files. 
#### Starting with an ID file:
It references the NCBI database, and if you put in a file the NCBI Mitochondrial Genbank IDs separated by lines, you must use the following command:
```
    $ python3 MPCreator.py -f ID_FILE_PATH -o OUTPUT_DIR_NAME -a ALIGNMENT_ID_NUMBER
```
#### Starting with a directory:
If you already have a directory with the Mitochondrial Genbank files, you must use the following command:
```
    $ python3 MPCreator.py -d DIR_PATH -o OUTPUT_DIR_NAME -a ALIGNMENT_ID_NUMBER
```
#### Parameters:
```
    -f or -d: You must choose between them, because '-f' starts the aplication reading a file with 
	      NCBI Mitochondrial IDs and '-d' starts the aplication reading a directory with Mitochondrial 
  	      genbanks files.

    -o : set the output diretory name at MPResults
    -a : set the alignment program by the ID.
         1 --> Mafft
         2 --> Muscle
         3 --> T_Coffee
```
