#!/usr/bin/env python3
# Name: Chetan Munugala(cmunugal)
# Group Members: none

'''This program reads in a FASTQ file and can run through it line by line
using the readFasta method. This program was made by modifying the program
"FASTAreader" made with the assistance of David Bernick. 
'''

class FastQreader :
    '''
    Class to provide reading of a file containing one or more FASTA
    formatted sequences:
    object instantiation:
    FastAreader(<file name>):
 
    object attributes:
    fname: the initial file name
 
    '''
    def __init__ (self, fname):
        '''contructor: saves attribute fname '''
        self.fname = fname

 
    def readFasta (self):
        '''
        using filename given in init, returns each included FastA record
        as 2 strings - header and sequence.
        whitespace is removed, no adjustment is made to sequence contents.
        The initial '>' is removed from the header.
        '''
        header = ''
        sequence = ''
        qualityscores = ''
        
        with open(self.fname) as fileH:
            # initialize return containers
            header = ''
            sequence = ''
            qualityscores = ''
 
            # skip to first fasta header
            line = fileH.readline()
            qualitysection = False
            while not line.startswith('@') :
                line = fileH.readline()
            header = line[1:].rstrip()
 
            # header is saved, get the rest of the sequence
            # up until the next header is found
            # then yield the results and wait for the next call.
            # next call will resume at the yield point
            # which is where we have the next header
            for line in fileH:
                if line.startswith ('@'):
                    yield header,sequence,qualityscores
                    header = line[1:].rstrip()
                    qualitysection = False
                    sequence = ''
                    qualityscores = ''
                else :
                    if line.startswith ('+'):
                        qualitysection = True
                    else:
                        if qualitysection == True:
                            qualityscores += ''.join(line.rstrip().split())
                        else:
                            sequence += ''.join(line.rstrip().split()).upper()
        # final header and sequence will be seen with an end of file
        # with clause will terminate, so we do the final yield of the data
        yield header,sequence,qualityscores
 
# presumed object instantiation and example usage
# myReader = FastAreader ('testTiny.fa');
# for head, seq in myReader.readFasta() :
#     print (head,seq)
