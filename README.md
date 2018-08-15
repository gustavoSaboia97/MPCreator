# MPCreator
MPCreator is a scientific workflow to control and automate the treatment of genomic metadata for phylogenomics analyses. 
## Location
MPCreator is available at: https://github.com/gustavoSaboia97/MPCreator .
## Docker Official Container
The command to pull the docker image is: 
```
   # docker pull saboia97/mpcreator 
```
## What MPCreator does?
MPCreator accepts as input an ID group, obtains the NCBI GenBank files (by the header) cleansing, filtering, and clustering metadata as localization, organism, gene, etc.Then, it organizes the sequences generating structured and organized files "by features" that can be used as input by phylogenetic programs such as RAxML/ExaML, PhyML, IQ-TREE, and BEAST.

To start that application, there is two ways
* Iterative with User by running:
```
    $ python3 MPCreator.py 

    (MCCreator requests  ID, output directory and the multiple sequence alignment)
```
* Automatic by running:
```
    $ python3 MPCreator.py IDList.txt

    (IDList.txt is the file containing IDs)
    When using this method to input the IDs, you must separate the IDs by lines.
```

### ID File Exemple
![alt text](img/IDFile-Exemple.png)
    

## Dependencies
* Python 3.X
* E-Direct (NCBI API)
* Muscle
* Mafft
* T_Coffee
* ClustalW