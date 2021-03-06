#!/usr/bin/env python3
import os
import sys
#run perf 5 times on each client file
#pid is a command line Input
os.system('sudo rm -rf Results')
os.system('sudo mkdir Results')
pid = sys.argv[1]
NO_OF_TESTS_EACH = 5
NO_OF_TESTS = 5
for _ in range(NO_OF_TESTS):
    fname = 'mkdir Results/Test_{}'.format(_)
    os.system(fname)
time = 30

for _ in range(NO_OF_TESTS):
    # Benchmarks
    print("Test {} Results".format(_))
    for i in range(NO_OF_TESTS_EACH):
        # No of tests
        print("Trial {}".format(i))
        perf_cmd = 'sudo taskset -c 32-95 sudo perf stat -e task-clock,context-switches,cpu-migrations,page-faults,cycles,instructions,cache-references,cache-misses,branches,branch-misses,L1-dcache-loads,L1-dcache-load-misses,L1-dcache-stores,L1-dcache-store-misses,L1-dcache-prefetches,L1-dcache-prefetch-misses,L1-icache-loads,L1-icache-load-misses,L1-icache-prefetches,L1-icache-prefetch-misses -p {} -- sleep {} 2>Results/Test_{}/Trial_{}.txt'.format(pid,time,_,i)
        client_cmd = 'sudo taskset -c 32-95 ./client.py {}'.format(_ + 1)
        net_cmd = perf_cmd + ' && ' + client_cmd
        # perf && client for simultaneous execution
        print(net_cmd)
        os.system(net_cmd)
