import statistics
from statistics import*
MERGE = 'merge'
merge_comp = 0
merge_comp_trial = []
merge_comp_avg = 0.0
merge_comp_std = 0.0
merge_cpu = 0.0
merge_cpu_trial = []
merge_cpu_avg = 0.0
merge_cpu_std = 0.0

QUICK_RAND = 'quickRand'
quickRand_comp = 0
quickRand_comp_trial = []
quickRand_comp_avg = 0.0
quickRand_comp_std = 0.0
quickRand_cpu = 0.0
quickRand_cpu_trial = []
quickRand_cpu_avg = 0.0
quickRand_cpu_std = 0.0

QUICK_DET = 'quickDet'
quickDet_comp = 0
quickDet_comp_trial = []
quickDet_comp_avg = 0.0
quickDet_comp_std = 0.0
quickDet_cpu = 0.0
quickDet_cpu_trial = []
quickDet_cpu_avg = 0.0
quickDet_cpu_std = 0.0
#PRE-
#POST-
def updateTrial(listName:str):
    global merge_comp
    global merge_comp_trial
    global merge_cpu
    global merge_cpu_trial
    global quickDet_comp
    global quickDet_comp_trial
    global quickDet_cpu
    global quickDet_cpu_trial
    global quickRand_comp
    global quickRand_comp_trial
    global quickRand_cpu
    global quickRand_cpu_trial 
    if listName.__eq__(MERGE):
        merge_comp_trial.append(merge_comp)
        merge_cpu_trial.append(merge_cpu)
        merge_comp = 0
        merge_cpu = 0.0
    elif listName.__eq__(QUICK_DET):
        quickDet_comp_trial.append(quickDet_comp)
        quickDet_cpu_trial.append(quickDet_cpu)
        quickDet_comp = 0
        quickDet_cpu = 0.0
    elif listName.__eq__(QUICK_RAND):
        quickRand_comp_trial.append(quickRand_comp)
        quickRand_cpu_trial.append(quickRand_cpu)
        quickDet_comp = 0
        quickDet_cpu = 0.0
#PRE-
#POST-
def genStats():
    global merge_comp_avg
    global merge_comp_std
    global merge_comp_trial
    global merge_cpu_avg
    global merge_cpu_std
    global merge_cpu_trial
    global quickDet_comp_avg
    global quickDet_comp_std
    global quickDet_comp_trial
    global quickDet_cpu_avg
    global quickDet_cpu_std
    global quickDet_cpu_trial
    global quickRand_comp_avg
    global quickRand_comp_std
    global quickRand_comp_trial
    global quickRand_cpu_avg
    global quickRand_cpu_std
    global quickRand_cpu_trial 
    #Calculate Means
    merge_comp_avg = mean(merge_comp_trial)
    merge_cpu_avg = mean(merge_cpu_trial)
    quickDet_comp_avg = mean(quickDet_comp_trial)
    quickDet_cpu_avg = mean(quickDet_cpu_trial)
    quickRand_comp_avg = mean(quickRand_comp_trial)
    quickRand_cpu_avg = mean(quickRand_cpu_trial)
    #Calculate Std Devs with population stand dev function from statistics
    merge_comp_std = pstdev(merge_comp_trial)
    merge_cpu_std = pstdev(merge_cpu_trial)
    quickDet_comp_std = pstdev(quickDet_comp_trial)
    quickDet_cpu_std = pstdev(quickDet_cpu_trial)
    quickRand_comp_std = pstdev(quickRand_comp_trial)
    quickRand_cpu_std = pstdev(quickRand_cpu_trial)

#PRE-
#POST-
def outputResults(outputFileName: str, listSize: int, random: float):
    global merge_comp_avg
    global merge_comp_std
    global merge_cpu_avg
    global merge_cpu_std
    global quickDet_comp_avg
    global quickDet_comp_std
    global quickDet_cpu_avg
    global quickDet_cpu_std
    global quickRand_comp_avg
    global quickRand_comp_std
    global quickRand_cpu_avg
    global quickRand_cpu_std
    #open output file and append to the end
    output = open(outputFileName, 'a')
    #print the listSize n and random p 
    print(listSize, random, file = output)
    #print avg and std info for comparison and cpu data from mergesort + quicksort
    print(f'\t{merge_comp_avg} {merge_comp_std} {merge_cpu_avg} {merge_cpu_std} ', file = output)
    print(f'\t {quickDet_comp_avg} {quickDet_comp_std} {quickDet_cpu_avg} {quickDet_cpu_std}', file = output)
    print(f'\t {quickRand_comp_avg} {quickRand_comp_std} {quickRand_cpu_avg} {quickRand_cpu_std}', file = output)
    print('', file = output)
    output.close()
#PRE-
#POST-
def resetAll():
    global merge_comp
    global merge_cpu
    global quickDet_comp
    global quickDet_cpu
    global quickRand_comp
    global quickRand_cpu
    global merge_comp_avg
    global merge_comp_std
    global merge_comp_trial
    global merge_cpu_avg
    global merge_cpu_std
    global merge_cpu_trial
    global quickDet_comp_avg
    global quickDet_comp_std
    global quickDet_comp_trial
    global quickDet_cpu_avg
    global quickDet_cpu_std
    global quickDet_cpu_trial
    global quickRand_comp_avg
    global quickRand_comp_std
    global quickRand_comp_trial
    global quickRand_cpu_avg
    global quickRand_cpu_std
    global quickRand_cpu_trial 
    merge_comp = 0
    merge_comp_trial.clear()
    merge_cpu = 0.0
    merge_cpu_trial.clear()
    quickDet_comp = 0
    quickDet_comp_trial.clear()
    quickDet_cpu = 0.0
    quickDet_cpu_trial.clear()
    quickRand_comp = 0
    quickRand_comp_trial.clear()
    quickRand_cpu = 0.0
    quickRand_cpu_trial.clear()

    merge_comp_avg = 0
    merge_comp_std = 0
    merge_cpu_avg = 0
    merge_cpu_std = 0

    quickDet_comp_avg = 0
    quickDet_comp_std = 0
    quickDet_cpu_avg = 0
    quickDet_cpu_std = 0

    quickRand_comp_avg = 0
    quickRand_comp_std = 0
    quickRand_cpu_avg = 0
    quickRand_cpu_std = 0