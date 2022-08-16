import math 
import random 
import time
import globals
from math import*
from random import*
NANO_TO_MILI = 1000
class sortList:
    nums = list()
    listName:str 
    def __init__(name:str):
        listName = name
    def cpu_time(sortAlg):#decorator for acquiring cpu time of each sorting algorithm 
        def setUp(*args, **kwargs):
            start = time.time()
            sortAlg(*args, **kwargs)
            stop = time.time()
            elapsed = (stop - start) * NANO_TO_MILI
            return elapsed
        return setUp
    #GENERIC SWAP METHOD
    def swap(self, ind1, ind2):
        temp = self.nums[ind1]
        self.nums[ind1] = self.nums[ind2]
        self.nums[ind2] = temp
    #CREATE RANDOM LIST WITH SIZE AND RANDOM FACTOR 
    def setList(self, size:int, randP: float):
        #set lists with the specific number of elements 
        self.nums = [i for i in range(size)]
        #round number of swaps based on size and randomness 
        numSwaps = round(size * randP)
        #for each swap
        for i in range(numSwaps):
            #find random indices to swap 
            while True:
                ind1 = randint(0, size - 1)
                ind2 = randint(0, size - 1)
                if ind1 != ind2:
                    break
            #update list with swaps
            self.swap(ind1, ind2)
    @cpu_time #decorator returns the cpu time that sorting algorithm required
    #MERGESORT ALGORITHM
    def mergeSort(self, start:int, end:int):
        self.mergeSortHelper(start, end)
    #RECURSIVE IMPLEMENTATION REQUIRES THIRD METHOD TO ACQUIRE ACCURATE CPU TIME 
    def mergeSortHelper(self, start: int, end:int):
        if start >= end:
            return
        mid = (start + end) // 2 #division but rounds down
        self.mergeSortHelper(start, mid)
        self.mergeSortHelper(mid + 1, end)
        self.merge(start, mid, end)
    def merge(self, start:int, mid:int, end:int):
        sizeList1 = mid - start + 1
        sizeList2 = end - mid
        list1 = list()
        list2 = list()
        ind1 = 0
        ind2 = 0
        indMerged = start
        #separate nums into 2 lists 
        for i in range(sizeList1):
            list1.append(self.nums[start + i])
        for j in range(sizeList2):
            list2.append(self.nums[mid + j + 1])
        #combine the lists together from least to most
        while (ind1 != sizeList1) & (ind2 != sizeList2): 
            #if the first list has the smallest element
            if list1[ind1] < list2[ind2]:
                #add it to the nums 
                self.nums[indMerged] = list1[ind1]
                ind1+=1
            #if the second list has the smallest element
            else: 
                #add it to the nums
                self.nums[indMerged] = list2[ind2]
                ind2+=1
            indMerged+=1
            globals.merge_comp+=1
        #check if one list has unadded elements 
        while ind1 != sizeList1:
            self.nums[indMerged] = list1[ind1]
            ind1+=1
            indMerged+=1
        while ind2 != sizeList2:
            self.nums[indMerged] = list2[ind2]
            ind2+=1
            indMerged+=1
    @cpu_time #decorator returns the cpu time that sorting algorithm required
    #QUICKSORT ALGORITHM UTILIZED BY BOTH RANDOM PIVOT AND DETERMINISTIC PIVOT QUICKSORT
    def quickSort(self, isRand:bool, start:int, end: int):
        global quickDet_comp
        global quickRand_comp
        if start >= end:
            return
        if isRand:#pivot for quickRand
            pivPos = start + (randint(0, end - start))
        else:#pivot for quickDet
            pivPos = end
        pivot = self.nums[pivPos]
        first = start
        last = end
        while(first <= last):
            while True:#do-while loop
                if isRand:
                    globals.quickRand_comp+=1
                else:
                    globals.quickDet_comp+=1
                if self.nums[first] < pivot:#even if false, comparison counted
                    first+=1
                else:
                    break#exits when nums[first] > pivot
            while True:#do while loop 
                if isRand:
                    globals.quickRand_comp+=1
                else:
                    globals.quickDet_comp+=1
                if self.nums[last] > pivot:#even if false, comparison counted
                    last-=1
                else:
                    break#exits when nums[last] < pivot
            if first <= last:#first must be less than last to swap because it indicates the list is not fully sorted yet
                self.swap(first, last)
                first+=1
                last-=1 
        self.quickSort(isRand, start, last)
        self.quickSort(isRand, first, end)

