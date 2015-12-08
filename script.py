#!/usr/bin/env python 
import sys
import re
import os 
inFilename = sys.argv[1]
if os.path.isfile(inFilename):
	namelength = inFilename.rfind(".")
	name = inFilename[0:namelength]
	exten = inFilename[namelength:]
	outFilename = "event_name"+exten

print "inFilename:", inFilename
print "outFilename:", outFilename

fpRead = open(inFilename, "r")
fpWrite = open(outFilename, "w+")

dcachePattern = re.complier(r'.*(dcache).*([0-9]+)')
icachePattern = re.complier(r'.*(icache).*([0-9]+)')
l2cachePattern = re.complier(r'.*(l2).*([0-9]+)')
tlbPattern = re.complier(r'.*(stage2_tlb).*([0-9]+)') 
dtbPattern = re.complier(r'.*(dtb).*([0-9]+)')
itbPattern = re.complier(r'.*(itb).*([0-9]+)')
threadbeginPattern = re.complier(r'.*Begin Simulation Statistics.*')
threadendPattern =re.complier(r'.*End Simulation Statistics.*')
lines = fpRead.readline()
#linesPattern = re.complier(r'(.*)(?=\s#)')

while lines:
	linesmatch = linesPatter.match(lines)
	dcachematch = dcachePattern.match(lines)
	icachematch = icachePattern.match(lines)
	l2match = l2cachePattern.match(lines)
	tlbmatch = tlbPattern.match(lines)
	dtbmatch = dtbPattern.match(lines)
	itbmatch = itbPattern.match(lines)
	threadbeginmatch = threadbeginPattern.match(lines)
	threadendmatch = threadendPattern.match(lines) 
	#lineswrite = linesmatch.group(1)

	if threadmatch:
		if dcachematch:
			fpWrite.write("%s " %(dcachematch.group(2)))
			continue
		if icachematch:
			fpWrite.write("%s " %(icachematch.group(2)))
			continue
		if l2match:
			fpWrite.write("%s " %(l2match.group(2)))
			continue
		if tlbmatch:
			fpWrite.write("%s " %(tlbmatch.group(2)))
			continue
		if dtbmatch:
			fpWrite.write("%s " %(dtbmatch.group(2)))
			continue
		if itbmatch:
			fpWrite.write("%s " %(itbmatch.group(2)))
			continue
	if threadendPattern:
		fpWrite.write("\n")
		continue
    lines = fpRead.readline()
fpRead.close()
fpWrite.close()
