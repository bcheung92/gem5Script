#!/usr/bin/env python
import sys
import re
import os
inFilename = sys.argv[1]
if os.path.isfile(inFilename):
	namelength = inFilename.rfind(".")
	name = inFilename[0:namelength]
	exten = inFilename[namelength:]
	outFilename = name+"-collect"+exten

print "inFilename:", inFilename
print "outFilename:", outFilename

fpRead = open(inFilename, "r")
fpWrite = open(outFilename, "w+")

dcachePattern = re.compile(r'.*(dcache).* ([0-9|\.]+)')
icachePattern = re.compile(r'.*(icache).* ([0-9|\.]+)')
l2cachePattern = re.compile(r'.*(l2).* ([0-9|\.]+)')
tlbPattern = re.compile(r'.*(stage2_tlb).* ([0-9|\.]+)')
dtbPattern = re.compile(r'.*(dtb).* ([0-9|\.]+)')
itbPattern = re.compile(r'.*(itb).* ([0-9|\.]+)')
threadbeginPattern = re.compile(r'.*Begin Simulation Statistics.*')
threadendPattern =re.compile(r'.*End Simulation Statistics.*')
lines = fpRead.readline()
#linesPattern = re.complier(r'(.*)(?=\s#)')

while lines:
#	linesmatch = linesPatter.match(lines)
	threadbeginmatch = threadbeginPattern.match(lines)
#	threadendmatch = threadendPattern.match(lines)
        #lineswrite = linesmatch.group(1)
        print "----------------------- reading lines------------------"
	if threadbeginmatch:
                print "------------------------ entering thread ------------------"
		threadlines = fpRead.readline()
#                print threadlines
#                dcachematch = dcachePattern.match(threadlines)
#                icachematch = icachePattern.match(threadlines)
#                l2match = l2cachePattern.match(threadlines)
#                tlbmatch = tlbPattern.match(threadlines)
#                dtbmatch = dtbPattern.match(threadlines)
#                itbmatch = itbPattern.match(threadlines)
#                threadendmatch = threadendPattern.match(threadlines)
		while threadlines:

#                print threadlines
                        dcachematch = dcachePattern.match(threadlines)
                        icachematch = icachePattern.match(threadlines)
                        l2match = l2cachePattern.match(threadlines)
                        tlbmatch = tlbPattern.match(threadlines)
                        dtbmatch = dtbPattern.match(threadlines)
                        itbmatch = itbPattern.match(threadlines)
                        threadendmatch = threadendPattern.match(threadlines)
#                        print threadlines
                        if dcachematch:
#                                print "dcachematch!!!"
				fpWrite.write("%s " %(dcachematch.group(2)))
			#	continue
			if icachematch:
				fpWrite.write("%s " %(icachematch.group(2)))
			#	continue
			if l2match:
				fpWrite.write("%s " %(l2match.group(2)))
			#	continue
			if tlbmatch:
#                               print "tlbmatch!!!"
				fpWrite.write("%s " %(tlbmatch.group(2)))
			#	continue
			if dtbmatch:
				fpWrite.write("%s " %(dtbmatch.group(2)))
			#	continue
			if itbmatch:
				fpWrite.write("%s " %(itbmatch.group(2)))
			#	continue
			if threadendmatch:
				fpWrite.write("\n")
                                print "------------------------ thread collection done!! --------------------"
				break
                        threadlines = fpRead.readline()
        lines = fpRead.readline()
fpRead.close()
fpWrite.close()
