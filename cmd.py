import subprocess
import os
import io
for i in xrange(1,26):
	os.system("./build/ALPHA_Network_test/gem5.debug configs/example/ruby_network_test.py --garnet-network=fixed --num-cpus=16 --num-dirs=16 --topology=Mesh --mesh-rows=4 --sim-cycles=100000 --injectionrate="+str(0.02*i)+" --synthetic=0")
	os.system("./my_scripts/extract_network_stats.sh && mv ./network_stats.txt ./network_stats_"+str(i)+".txt")
	os.system("grep average_latency network_stats_"+str(i)+".txt >> average_latency_report.txt")

