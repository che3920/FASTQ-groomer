# FASTQ-groomer

Here is software for my version of the FASTQ groomer application that converts between DNA quality score variations. 


Instructions for the program:

This program inputs a FASTQ file as well as the input format and the desired
output format. Inputs and outputs must be entered exactly as listed below
(see input options and output options). Basically, this program converts the
FASTQ file inputted by the user into either Phred64 or Phred33 format, depending
on what the user desires. THIS PROGRAM IS NOT A COMMAND LINE PROGRAM.

Input options:
Phred33
Sanger
Phred64
Phred64B
Solexa

Output options:
Phred33
Phred64


The program itself is called groomer.py but requires the FastQreader.py in the same folder to import. Two input files have been provided for testing (Phred64Input.txt and testSolexa.fastq.txt) that are in Phred64 and Solexa formats respectively. 

If the user is not familiar with FASTQ format, the website below can explain it. 
https://en.wikipedia.org/wiki/FASTQ_format

This program was made with assistance from David Bernick.
