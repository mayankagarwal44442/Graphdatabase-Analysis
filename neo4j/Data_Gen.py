import csv
import sys

def IC_Write(Instruction_count,NO_OF_TESTS):
    CSV_File = 'Instruction_Count.csv'
    Headers = ['Query No.','Trial 1','Trial 2','Trial 3','Trial 4','Trial 5']
    with open(CSV_File,'a+',newline='\n') as csv_file:
        csvwriter = csv.writer(csv_file)
        for _ in range(NO_OF_TESTS):
            Instruction_count[_].insert(0,_ + 1)
        csvwriter.writerow(Headers)
        csvwriter.writerows(Instruction_count)

def IPC_Write(Ins_per_cycle,NO_OF_TESTS):
    CSV_File = 'Instruction_Per_Cycle.csv'
    Headers = ['Query No.','Trial 1','Trial 2','Trial 3','Trial 4','Trial 5']
    with open(CSV_File,'a+',newline='\n') as csv_file:
        csvwriter = csv.writer(csv_file)
        for _ in range(NO_OF_TESTS):
            Ins_per_cycle[_].insert(0,_ + 1)
        csvwriter.writerow(Headers)
        csvwriter.writerows(Ins_per_cycle)

def CR_Write(Cache_References,NO_OF_TESTS):
    CSV_File = 'Cache_References.csv'
    Headers = ['Query No.','Trial 1','Trial 2','Trial 3','Trial 4','Trial 5']
    with open(CSV_File,'a+',newline='\n') as csv_file:
        csvwriter = csv.writer(csv_file)
        for _ in range(NO_OF_TESTS):
            Cache_References[_].insert(0,_ + 1)
        csvwriter.writerow(Headers)
        csvwriter.writerows(Cache_References)

def LDL_Write(L1_dcache_loads,NO_OF_TESTS):
    CSV_File = 'L1_dcache_loads.csv'
    Headers = ['Query No.','Trial 1','Trial 2','Trial 3','Trial 4','Trial 5']
    with open(CSV_File,'a+',newline='\n') as csv_file:
        csvwriter = csv.writer(csv_file)
        for _ in range(NO_OF_TESTS):
            L1_dcache_loads[_].insert(0,_ + 1)
        csvwriter.writerow(Headers)
        csvwriter.writerows(L1_dcache_loads)

def LDM_Write(L1_dcache_loads_misses,NO_OF_TESTS):
    CSV_File = 'L1_dcache_loads_misses.csv'
    Headers = ['Query No.','Trial 1','Trial 2','Trial 3','Trial 4','Trial 5']
    with open(CSV_File,'a+',newline='\n') as csv_file:
        csvwriter = csv.writer(csv_file)
        for _ in range(NO_OF_TESTS):
            L1_dcache_loads_misses[_].insert(0,_ + 1)
        csvwriter.writerow(Headers)
        csvwriter.writerows(L1_dcache_loads_misses)

NO_OF_TESTS = 5
NO_OF_TESTS_EACH = 5

origin_path_neo4j = 'D:\\College\\PES\\Semester-6\\Cloud - Computing\\Graphdatabase-Analysis\\neo4j\Results\\'
origin_path_postgres = 'D:\\College\\PES\\Semester-6\\Cloud - Computing\\Graphdatabase-Analysis\\postgres\Results\\'

if (sys.argv[0] == 1):
    origin_path = origin_path_neo4j
else:
    origin_path = origin_path_postgres

IC = []
IPC = []
CR = []
LDL = []
LDM = []

for query in range(NO_OF_TESTS):
    # Data Storage for each Test Case
    Instruction_count = []
    Ins_per_cycle = []
    Cache_References = []
    L1_dcache_loads = []
    L1_dcache_loads_misses =[]
    for trial in range(NO_OF_TESTS_EACH):
        File_name = origin_path + 'Test_{}\\Trial_{}.txt'.format(query,trial)
        File = open(File_name,"r")
        # Every Line of the file
        Lines = File.readlines()
        # Data Collection - Split by !
        Instruction = '!'.join(Lines[8].strip().split()).split('!')
        Instruction_count.append(Instruction[0].replace(",",""))
        Ins_per_cycle.append(Instruction[3])
        Cache_Reference = '!'.join(Lines[9].strip().split()).split('!')
        Cache_References.append(Cache_Reference[0].replace(",",""))
        L1_dcache_load = '!'.join(Lines[13].strip().split()).split('!')
        L1_dcache_loads.append(L1_dcache_load[0].replace(",",""))
        L1_dcache_loads_miss = '!'.join(Lines[14].strip().split()).split('!')
        L1_dcache_loads_misses.append(L1_dcache_loads_miss[0].replace(",",""))
    print(Instruction_count)
    IC.append(Instruction_count)
    print(Ins_per_cycle)
    IPC.append(Ins_per_cycle)
    print(Cache_References)
    CR.append(Cache_References)
    print(L1_dcache_loads)
    LDL.append(L1_dcache_loads)
    print(L1_dcache_loads_misses)
    LDM.append(L1_dcache_loads_misses)
    print('__________________________________________________________________________________________________________________')
#print(IC)
IC_Write(IC,5)
IPC_Write(IPC,5)
CR_Write(CR,5)
LDL_Write(LDL,5)
LDM_Write(LDM,5)
