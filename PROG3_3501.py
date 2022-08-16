#Author: Nico Bokhari 
#Creation Date: 5-23-2022
#Purpose: Code for experimental data on time complexity analysis of sorting algorithms 
# relative to list size and randomness. 
# Max list length is n = 498, otherwise a RecursionError occurs
# Opportunity for non-recursive version of mergesort and quicksort
import globals
import sortList
from sortList import*

def main():
    listSizes = []
    randomFactors = []
    numTrials = 0
    #OPEN INPUT FILE
    inputFileName = 'input.txt'
    outputFileName = 'output.txt'
    with open(inputFileName) as inputFile:
        #loop over lines in inputFile
        for line in inputFile:
            #strip leading and trailing whitespace
            line = line.strip()
        #SPLIT LINE INTO TOKENS FOR LINE
            marker = ''
            tokens = []
            for token in line.split():
                #trim whitespace in each token
                token = token.strip()
                #add token to tokens
                tokens.append(token)
        #END OF LINE SPLITTING FOR TOKENS
            
        #EVALAUTE TOKENS FOR LINE
            if(len(tokens) > 0): #first token denotes whether line is list sizes or randomness factors p 
                marker = tokens[0]
                if(len(tokens) > 1): #if more tokens after marker
                    if marker.casefold() == 'n': #if marker denotes listsizes
                        #set listSizes to the rest of the tokens
                        listSizes = tokens[1:len(tokens)]
                        #convert from string to int list
                        listSizes = list(map(int, listSizes))
                    if marker.casefold() == 'p': #if marker denotes randomness factor
                        #set randomFactors to the rest of the tokens 
                        randomFactors = tokens[1:len(tokens)]
                        #convert from string to float list
                        randomFactors = list(map(float, randomFactors))
                    if marker.casefold() == 't': #if marker denotes number of trials
                        #set numTrials to second token 
                        numTrials = int(tokens[1])
                if marker.casefold() == 'run':
                    if not len(listSizes) or not len(randomFactors): #if listSizes or randomFactors are empty
                        print('Error: Cannot Run Experiment. Missing list lengths n or random factors p')
                        break #Exit inputFile
        #END OF TOKEN EVALUATION

        #CLOSE INPUT FILE 
        inputFile.close()
        runExp(listSizes, randomFactors, numTrials)

def runExp(listSizes:list, randomFactors:list, numTrials:int):
    #Create/Open output file
    outputFileName = 'output.txt'
    #Clear the contents of the file before outputing results 
    open(outputFileName, 'w').close()
    #Create sortList objects merge, quickDet, quickRand
    merge = sortList()
    quickDet = sortList()
    quickRand = sortList()
    #for each listSize
    for n in listSizes:
        for p in randomFactors:
            #create the randomized lists with size n and randomization p
            for i in range(numTrials):
                merge.setList(n,p)
                quickDet.setList(n,p)
                quickRand.setList(n,p)
                globals.merge_comp = merge.mergeSort(0, n - 1)
                globals.quickDet_comp = quickDet.quickSort(False, 0, n - 1)
                globals.quickRand_comp = quickRand.quickSort(True, 0, n - 1)
                globals.updateTrial(globals.MERGE)
                globals.updateTrial(globals.QUICK_DET)
                globals.updateTrial(globals.QUICK_RAND)
            globals.genStats()
            globals.outputResults(outputFileName, n, p)
            globals.resetAll()
    print('Success')
        
if __name__ == '__main__': 
    main()