#!/usr/bin/env python
import sys
import re
import os
#inFilename = sys.argv[1]
statsFile = sys.argv[1]
pidFile = sys.argv[2]
if os.path.isfile(inFilename):
	namelength = statsFile.rfind(".")
	name = statsFile[0:namelength]
	exten = statsFile[namelength:]
	outFilename = name+"-collect-samepid"+exten

print "inFilename:", statsFile,pidFile
print "outFilename:", outFilename

statsRead = open(statsFile, "r")
pidRead = open(statsFile,"r")
fpWrite = open(outFilename, "w+")
## set a flag to confirm if break or not
#flag=0 

threadbeginPattern = re.compile(r'.*Begin Simulation Statistics.*')
threadendPattern =re.compile(r'.*End Simulation Statistics.*')
pidPattern = re.compile(r'.*next_pid=(-?[0-9]+).*')
l2overallmissPattern = re.compile(r'(system.l2.overall_misses).*(total).* ([0-9|\.]+)') 
l2overallmisslatencyPattern =re.compile(r'(system.l2.overall_miss_latency).*(total).* ([0-9|\.]+)')
pidlines = pidRead.readline()
statslines = statsRead.readline()
# while pidlines:
# 	print "------------loading the pidFile---------------- "
# 	pidmatch = pidPattern.match(pidlines)
# 	statslines = statsRead.readline()
# 	if pidmatch:
# 		fpWrite.write("%s " pidmatch.group(1))
# 		while statslines:
# 			#flag = 0 
# 			print "-------------loding the statsFile-----------------"
# 			threadbeginmatch = threadbeginPattern.match(statslines)
# 			if threadbeginmatch:
# 	            print "------------------------ entering thread -------------------"
# 				threadlines = statsRead.readline()
# 				while threadlines:
# 					l2overallmissmatch = l2overallmissPattern.match(threadlines)
# 					l2overallmisslatencymatch = l2overallmisslatencyPattern.match(threadlines)
# 		            threadendmatch = threadendPattern.match(threadlines)
# 					if l2overallmissmatch:
# 						print "l2overallmissmatch!!!"
# 						fpWrite.write("%s " %(l2overallmissmatch.group(3)))
# 					if l2overallmisslatencymatch:
# 						print "l2overallmisslatencymatch!!!"
# 						fpWrite.write("%s " %(l2overallmisslatencymatch.group(3)))
# 					if threadendmatch:
# 						fpWrite.write("\n")
# 						flag = 1
# 		                print "---------------thread collection done!!!--------------"
# 						break
# 		            threadlines = statsRead.readline()
# 		    if flag == 1:
# 		        	break
# 	pidlines = pidRead.readline()
while statslines:
	threadbeginmatch = threadbeginPattern.match(statslines)
	print "-------------loding the statsFile-----------------"
	if threadbeginmatch:
		print "-----------------readling theadlines----------------"
		threadlines = statsRead.readline()
		while threadlines:
			l2overallmissmatch = l2overallmissPattern.match(threadlines)
			l2overallmisslatencymatch = l2overallmisslatencyPattern.match(threadlines)
			threadendmatch = threadendPattern.match(threadlines)
			if l2overallmissmatch:
				print "l2overallmissmatch!!!"
				fpWrite.write("%s " %(l2overallmissmatch.group(3)))
			if l2overallmisslatencymatch:
				print "l2overallmisslatencymatch!!!"
				fpWrite.write("%s " %(l2overallmisslatencymatch.group(3)))
			if threadendmatch:
				print "------------------thread collection done!!!------------"
				pidmatch = pidPattern.match(pidlines)
				fpWrite.write("%s \n" %pidmatch.group(1))
				pidlines=pidRead.readline()
				break
		threadlines=statsRead.readline()	

statsRead.close()
pidRead.close()
fpWrite.close()
