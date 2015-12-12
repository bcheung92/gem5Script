#!/usr/bin/env python
import sys
import re
import os
inFilename = sys.argv[1]
if os.path.isfile(inFilename):
	namelength = inFilename.rfind(".")
	name = inFilename[0:namelength]
	exten = inFilename[namelength:]
	outFilename = name+"-collect-special"+exten

print "inFilename:", inFilename
print "outFilename:", outFilename

fpRead = open(inFilename, "r")
fpWrite = open(outFilename, "w+")


dcachemissPattern = re.compile(r'.*(dcache.overall_misses).*(total).* ([0-9|\.]+)') #overall dcache misses
dcachemshrPattern = re.compile(r'.*(dcache.overall_mshr).*(total).* ([0-9|\.]+)') #overall dcache MSHR misses
icachemissPattern = re.compile(r'.*(icache.overall_misses).*(total).* ([0-9|\.]+)') #overall icache misses
icachemshrPattern = re.compile(r'.*(icache.overall_mshr).*(total).* ([0-9|\.]+)') #overall icache MSHR misses
l2cachemissPattern = re.compile(r'.*(l2.overall_misses).*(total).* ([0-9|\.]+)')#overall l2cache misses
l2cachemshrPattern = re.compile(r'.*(l2.overall_mshr).*(total).* ([0-9|\.]+)')# overall l2 MSHR misses
dtbmissPattern = re.compile(r'.*(dtb.misses).* ([0-9|\.]+)')
itbmissPattern = re.compile(r'.*(itb.misses).* ([0-9|\.]+)')
# dcachePattern = re.compile(r'.*(dcache).* ([0-9|\.]+)')
# icachePattern = re.compile(r'.*(icache).* ([0-9|\.]+)')
# l2cachePattern = re.compile(r'.*(l2).* ([0-9|\.]+)')
# tlbPattern = re.compile(r'.*(stage2_tlb).* ([0-9|\.]+)')
# dtbPattern = re.compile(r'.*(dtb).* ([0-9|\.]+)')
# itbPattern = re.compile(r'.*(itb).* ([0-9|\.]+)')
threadbeginPattern = re.compile(r'.*Begin Simulation Statistics.*')
threadendPattern =re.compile(r'.*End Simulation Statistics.*')
lines = fpRead.readline()
# #linesPattern = re.complier(r'(.*)(?=\s#)')

while lines:
#	linesmatch = linesPatter.match(lines)
	threadbeginmatch = threadbeginPattern.match(lines)
#	threadendmatch = threadendPattern.match(lines)
        #lineswrite = linesmatch.group(1)
        print "----------------------- reading lines------------------"
	if threadbeginmatch:
                print "------------------------ entering thread -------------------"
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
#           print threadlines
			dcachemissmatch = dcachemissPattern.match(threadlines)
			dcachemshrmatch = dcachemshrPattern.match(threadlines)
			icachemissmatch = icachemissPattern.match(threadlines)
			icachemshrmatch = icachemshrPattern.match(threadlines)
			l2cachemissmatch = l2cachemissPattern.match(threadlines)
			l2cachemshrmatch = l2cachemissPattern.match(threadlines)
			dtbmissmatch = dtbmissPattern.match(threadlines)
			itbmissmatch = itbmissPattern.match(threadlines)
            # dcachematch = dcachePattern.match(threadlines)
            # icachematch = icachePattern.match(threadlines)
            # l2match = l2cachePattern.match(threadlines)
            # tlbmatch = tlbPattern.match(threadlines)
            # dtbmatch = dtbPattern.match(threadlines)
            # itbmatch = itbPattern.match(threadlines)
                        threadendmatch = threadendPattern.match(threadlines)
#           print threadlines
                        if dcachemissmatch:
				print "dcachemissmatch!!!"
				fpWrite.write("%s " %(dcachemissmatch.group(3)))
			#	continue
			if dcachemshrmatch:
				print "dcachemshrmatch!!!"
				fpWrite.write("%s " %(dcachemshrmatch.group(3)))
			#	continue
			if icachemissmatch:
				print "icachemissmatch!!!"
				fpWrite.write("%s " %(icachemissmatch.group(3)))
			#	continue
			if icachemshrmatch:
                                print "icachemshrmatch!!!"
				fpWrite.write("%s " %(icachemshrmatch.group(3)))
			#	continue
			if l2cachemissmatch:
				print "l2cachemissmatch!!!"
				fpWrite.write("%s " %(l2cachemissmatch.group(3)))
			#	continue
			if l2cachemshrmatch:
				print "l2cachemshrmatch!!!"
				fpWrite.write("%s " %(l2cachemshrmatch.group(3)))
			#	continue
			if dtbmissmatch:
				print "dtbmissmatch!!!"
				fpWrite.write("%s " %(dtbmissmatch.group(2)))
			if itbmissmatch:
				print "itbmissmatch!!!"
				fpWrite.write("%s " %(itbmissmatch.group(2)))
			if threadendmatch:
				fpWrite.write("\n")
                                print "------------------------ thread collection done!! --------------------"
				break
                threadlines = fpRead.readline()
        lines = fpRead.readline()
fpRead.close()
fpWrite.close()
