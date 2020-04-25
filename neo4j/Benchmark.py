import os
import sys
# run perf 5 times on each client file

os.system('rm -rf Results')
os.system('mkdir Results')
NO_OF_TESTS_EACH = 1
NO_OF_TESTS = 5
app_pid_file = open('app_pid','r')
pid_list = app_pid_file.read()

for _ in range(NO_OF_TESTS):
    fname = 'sudo mkdir perf_curr_res/Test_{}'.format(_)
    os.system(fname)
time = 30

for _ in range(NO_OF_TESTS):
    # Benchmarks
    print("Test {} Results".format(_))
    for i in range(NO_OF_TESTS_EACH):
        # No of tests
        print("Trial {}".format(i))
        perf_cmd = 'sudo taskset -a -c 24-47,72-95 sudo perf stat -e task-clock,context-switches,cpu-migrations,page-faults,cycles,instructions,cache-references,cache-misses,branches,branch-misses,L1-dcache-loads,L1-dcache-load-misses,L1-dcache-stores,L1-dcache-store-misses,L1-dcache-prefetches,L1-dcache-prefetch-misses,L1-icache-loads,L1-icache-load-misses,L1-icache-prefetches,L1-icache-prefetch-misses -p {} -- sleep {} 2>perf_new_res/Test_{}/Trial_{}.txt'.format(pid_list,
            time,_, i)
        client_cmd = 'sudo taskset -a -c 24-47,72-95 python3 client.py {}'.format(_ + 1)
        net_cmd = perf_cmd + ' && ' + client_cmd
        # perf && client for simultaneous execution
        print(net_cmd)
        os.system(net_cmd)
