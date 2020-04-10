#!/usr/bin/env python3
# Name: Chetan Munugala(cmunugal)
# Group Members: none

import FastQreader

'''
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



Pseudocode

class Groomer:

in init:
dictionaries for all the conversions between formats

method for 64to33

method for 33to64

method for 64to64

method for 33to33

method for 64Bto64

method for 64Bto33

method for Solexato33

method for Solexato64

outside of groomer class:
create groomer object with desired format and file format parameters
call the methods based on conditionals

example:
if this format:
    call method to convert to that format

print in proper format for desired format

'''
class Groomer:

    def __init__ (self,fileformat,desiredformat): #initializes groomer object with desiredformat and file format
        self.fileformat = fileformat
        self.desiredformat = desiredformat

        #below are all the dictionaries for conversions between formats
        #some inverse dictionaries exist for testing correct conversions
        
        phred33Sanger = {'!':0,'"':1, '#':2, '$':3, '%':4, '&':5, "'":6, '(':7, ')':8, '*':9,
                 '+':10, ',':11, '-':12, '.':13, '/':14, '0':15, '1':16, '2':17, '3':18,
                 '4':19, '5':20, '6':21, '7':22, '8':23, '9':24, ':':25, ';':26, '<':27,
                 '=':28, '>':29, '?':30, '@':31, 'A':32, 'B':33, 'C':34, 'D':35, 'E':36,
                 'F':37, 'G':38, 'H':39, 'I':40}
        self.phred33Sanger = phred33Sanger

        phred64 ={'@':0, 'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9,
                 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18,
                 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26, '[':27, 
                 "\\":28, ']':29, '^':30, '_':31, '`':32, 'a':33, 'b':34, 'c':35, 'd':36,
                 'e':37, 'f':38, 'g':39, 'h':40}
        self.phred64 = phred64

        invphred64 = {v:k for k,v in phred64.items()}
        self.invphred64 = invphred64

        invphred33Sanger = {v:k for k,v in phred33Sanger.items()}
        self.invphred33Sanger = invphred33Sanger

        solto33 = {';':'"', '<':'"', '=':'#', '>':'#', '?':'$', '@':'$', 'A':'%',
                   'B':'%', 'C':'&', 'D':'&', 'E':"'", 'F':'(', 'G':')', 'H':'*',
                   'I':'+', 'J':'+', 'K':',', 'L':'-', 'M':'.', 'N':'/', 'O':'0',
                   'P':'1', 'Q':'2', 'R':'3', 'S':'4', 'T':'5', 'U':'6', 'V':'7',
                   'W':'8', 'X':'9', 'Y':':', 'Z':';', '[':'<', '\\':'=',']':'>',
                   '^':'?', '_':'@', '`':'A', 'a':'B', 'b':'C', 'c':'D', 'd':'E',
                   'e':'F', 'f':'G', 'g':'H', 'h':'I'}
        self.solto33 = solto33

        solto64 = {';':'A', '<':'A', '=':'B', '>':'B', '?':'C', '@':'C', 'A':'D',
                   'B':'D', 'C':'E', 'D':'E', 'E':"F", 'F':'G', 'G':'H', 'H':'I',
                   'I':'J', 'J':'J', 'K':'K', 'L':'L', 'M':'M', 'N':'N', 'O':'O',
                   'P':'P', 'Q':'Q', 'R':'R', 'S':'S', 'T':'T', 'U':'U', 'V':'V',
                   'W':'W', 'X':'X', 'Y':'Y', 'Z':'Z', '[':'[', '\\':'\\',']':']',
                   '^':'^', '_':'_', '`':'`', 'a':'a', 'b':'b', 'c':'c', 'd':'d',
                   'e':'e', 'f':'f', 'g':'g', 'h':'h'}
        self.solto64 = solto64

        offsetB ={'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9,
                  'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18,
                  'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26, '[':27, 
                  "\\":28, ']':29, '^':30, '_':31, '`':32, 'a':33, 'b':34, 'c':35, 'd':36,
                  'e':37, 'f':38, 'g':39, 'h':40}


    def groom33to64(self,qual): #converts from Phred33 to Phred64
        newqual = ''
        for score in qual:
            if score in self.phred33Sanger.keys():
                newqual = newqual + self.invphred64[self.phred33Sanger[score]]
        return(newqual)


    def groom64to33(self,qual): #converts from Phred64 to Phred33
        newqual = ''
        for score in qual:
            if score in self.phred64.keys():
                newqual = newqual + self.invphred33Sanger[self.phred64[score]]
        return(newqual)

    
    def groom64Bto33(self,qual): #converts from Phred64B to Phred33
        newqual = ''
        for score in qual:
            if score in self.offsetB.keys():
                newqual = newqual + self.invphred33Sanger[self.offsetB[score]]
        return(newqual)

    def groom64Bto64(self,qual): #converts from Phred64B to Phred64
        return qual

    def groomSolto33(self,qual): #converts from Solexa to Phred33
        newqual = ''
        for score in qual:
            if score in self.solto33.keys():
                newqual = newqual + self.solto33[score]
        return(newqual)

    def groomSolto64(self,qual): #converts from Solexa to Phred64
        newqual = ''
        for score in qual:
            if score in self.solto64.keys():
                newqual = newqual + self.solto64[score]
        return(newqual)


fileformat = input("Enter format of input file:") #three lines that prompt user for input format, output format, and filename
desiredformat = input("Enter desired output format:")
filename = input("Enter name of file:")
myReader = FastQreader.FastQreader (filename)
myGroomer = Groomer(fileformat,desiredformat)
for head,seq,qual in myReader.readFasta(): #iterates through every fastq sequence in file
    head = '@' + head
    print(head)
    print(seq)
    if desiredformat == 'Phred64':
        head = head[1:]
        head = '+' + head
        print(head)
        if fileformat == 'Phred33' or fileformat == 'Sanger':
            newqual = myGroomer.groom33to44(qual)
        if fileformat == 'Phred64':
            newqual = qual
        if fileformat == 'Phred64B':
            newqual = qual
        if fileformat == 'Solexa':
            newqual = myGroomer.groomSolto64(qual)

    if desiredformat == 'Phred33':
        print('+')
        if fileformat == 'Phred33' or fileformat == 'Sanger':
            newqual = qual
        if fileformat == 'Phred64':
            newqual = myGroomer.groom64to33(qual)
        if fileformat == 'Phred64B':
            newqual = myGroomer.groom64Bto33(qual)
        if fileformat == 'Solexa':
            newqual = myGroomer.groomSolto33(qual)
        
            
    print(newqual)




