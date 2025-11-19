## Making models of Vital et al butyrate synthesis pathway enzymes
### ColabFold_ButGenesDB_Notebook.html
#### 2024-10-15
#### Markdown and content author: Chad Masarweh

Goal for this document: I created this as an easy-to-read and reproducable documentation and short explanation of how I used ColabFold to model each unique protein sequence in Vital et al.’s (DOI: https://doi.org/10.1128/msystems.00130-17) butyrate synthesis pathway enzymes database. To save time, I didn’t try very hard to explain the code, so please let me know if something is broken, stupid, or confusing.

-----

## Quantitative mapping metagenome reads to a reference database
### Quant_Fxnl_Meta_Wrkflw_reads.html
#### 2024-09-17
#### Markdown author: Chad Masarweh
#### Content authors: Zeya Xue, Michelle Treiber, Yirui Tang Villanueva, Chad Masarweh, Andrew Oliver

Goal: While making this, I was thinking, “What resource do I wish I had when I was adapting other people’s workflows?” So that’s what this is, a reference document for a programatic way of quantifying metagenome genes that can be chopped up and adapted. It also happened to be a way for me to teach myself what every line of the code does. It’s less of a tutorial and more of a self-contained and (fully?) reproducible documentation of my actual work. I tried to keep it modular so you, the reader, can bring the modules into your own workflow and easily change them. Thus, this document does not break down a single shell script, and it is meant to be run interactively. As such, I explain most of the lines of code so that you can modify them more easily.

Directions: Put the scripts that I attached in your ${scripts} directory and put the fasta file I attached in your ${DB_DIR} directory (see Step 1). Read this document and run in New Spitfire the red-outlined code chunks with the header “Run this”. Compare your inputs and outputs to what I show in the document. Try to adapt it to your workflow if you want. Come to the GFWG meeting with confusions, questions, criticisms, suggestions, changes, and additions. I’ve never made anything like this before, so it’s a work in progress. This document uses Spitfire’s Anaconda, but if you have your own way of software version control, use that, you just need Python and Pandas for part 1. If you’re not comfortable in the Unix terminal and you want to be, do the Unix and Linux material at http://korflab.ucdavis.edu/Unix_and_Perl/index.html. This document assumes that you have a basic comfort in Unix and Linux, but you could probably run all the code knowing very little.

Context: This document explains my workflow for quantifying reads of butyrate synthesis pathway genes in FL100 metagenomes. It uses a subsample of the reference database and a subsample of the FL100 metagenomes. I tried to make this workflow adaptable to any amino acid reference database and any short-reads metagenome set. If you do not finish this workflow in one session, make sure to redefine the variables in Step 1 “Set up your environment” and in steps you already completed.

-----

## Quantitative mapping metagenome reads to annotated metagenome ORFs
### Quant_Fxnl_Meta_Wrkflw_orfs2.html
#### 2024-10-03
#### RMarkdown author: Chad Masarweh
#### Content authors: Chad Masarweh, Michelle Treiber, Zeya Xue, Andrew Oliver, dbCAN3 people (Le Huang, Jinfang Zheng, Haidong Yi, Qiwei Ge, Tanner Yohe)

This document explains my workflow for quantifying reads representing coding sequences of butyrate synthesis pathway genes in assembled FL100 metagenomes. It is based on the dbCAN tutorial, Module 3 (thank you to Andrew for telling me about it). This is because the dbCAN3 pipeline uses three methods for annotating ORFs: DIAMOND BLAST, HMMER, and their own eCAMI. Their recommendation is to trust an annotation on which at least 2/3 methods agree. So, if for some reason you must start with the metagenome assembly, rather than the metagenome reads, you would need to use the workflow in this document.
The Python scripts are all my own, but they are simple and can probably be done in R. This document uses a subsample of the reference database and a subsample of the FL100 metagenomes. I tried to make this workflow applicable to any amino acid reference database and any set of short-reads metagenomes assembled with a k-mer method.
The code blocks I actually ran are outlined in red and are titled “Run this” and have a button to copy the code to your clipboard

-----

## Making HMMs for Vital et al butyrate synthesis pathway genes
### makingButSyntPathGenesHMMs.html
#### 2024-09-24
#### RMarkdown and Content author: Chad Masarweh

Goal for this document: I created this as an easy-to-read and reproducable documentation and short explanation of how I built HMMER-formatted HMMs of each enzyme function in Vital et al.’s (DOI: https://doi.org/10.1128/msystems.00130-17) butyrate synthesis pathway genes database. To save time, I didn’t try very hard to explain the code, so please let me know if something is broken, stupid, or confusing.
Directions: read this document and run in New Spitfire the red-outlined code chunks with the header “Run this”. Change it and add to it to make it your own. You could use Old Spitfire, too, because this workflow does not require that many cores, but if your MSAs are rather large and you want to use GNU parallel, use New Spitfire so you dont dominate Old Spitfire.

The Python scripts are all my own. I tried a little bit to make this workflow applicable to any collection of related genes and any set of short-reads metagenomes assembled with a k-mer method, but there are some hard-coded format expectations, such as enzyme functions being denoted in fasta headers as “function%restOfFastaHeader”.

-----

## Dietary and biomarker predictors of CACO-2 barrier function and inflammation: preparing data for analysis
### 1_CACO2_permeability-data_preparation.html
#### 2025-11-19
#### RMarkdown and Content author: Chad Masarweh

Preparing untidy data for analysis, mergiing with the metadata, and adding columns for logistic regression and random forest.
