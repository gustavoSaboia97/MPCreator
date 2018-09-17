# MPCreator
MPCreator is a scientific workflow to control and automate the treatment of genomic metadata for phylogenomics analyses. 
## Location
MPCreator is available at: https://github.com/gustavoSaboia97/MPCreator .
## Docker Official Container
The command to pull the docker image is: 
```
   # docker pull saboia97/mpcreator 
```

Starting with an ID file:
```
    $ python3 MPCreator.py -f ID_FILE_PATH -o OUTPUT_DIR_NAME -a ALIGNMENT_ID_NUMBER
```
Starting with a directory:
```
    $ python3 MPCreator.py -d DIR_PATH -o OUTPUT_DIR_NAME -a ALIGNMENT_ID_NUMBER
```
Parameters:
```
    -f or -d: You must choose between them, because '-f' starts the aplication reading a file with NCBI Mitochondrial IDs and '-d' starts the aplication reading a directory with Mitochondrial genbanks files

    -o : set the output diretory name at MPResults
    -a : set the alignment program.
         1 --> Mafft
         2 --> Muscle
         3 --> T_Coffee
```
