#!/usr/bin/env python
import sys
import re
import os
inFilename = sys.argv[1]
if os.path.isfile(inFilename):
    namelength = inFilename.rfind(".") # find . index to note the length of the inputfile,the length of the input file doesn't include the extension
    name = inFilename[0:namelength] # the name of the  input file 
    exten = inFilename[namelength:]   # the extension of the input file 
    outFilename =  "conflict_distribute" + exten # define the outfile

#print the file name  
print "inFilename:", inFilename 
print "outFilename:", outFilename

#to develop a read and wite object 
length=100
fpRead = open(inFilename, "r")
fpWrite = open(outFilename, "w+")

#to develop the re pattern
                                                                                                    
#linePattern = re.compile(r'.*(Original_Cache_Trace)(::)([0-9]+)(\s+)([0-9]+)(\s+)')
linePattern = re.compile(r'.*(system.cpu0.dcache.original_stack_distribute::samples)(\s+)([0-9]+)')
linePattern1 = re.compile(r'.*(system.cpu0.dcache.original_stack_distribute::)([0-9]+)(\s+)([0-9]+)')
lines = fpRead.readline()
while lines:
#print lines.split(',')[1]
    match1 = linePattern.match(lines)
    if match1:
#        fpWrite.write("%s \t" %match1.group(3))
	other=int(match1.group(3))
#	print other
	k=0
        distance_last=-1
        for i in range(0,length):
            if k>length-2:
	        break
	    lines = fpRead.readline()
    	    match2 = linePattern1.match(lines)
	    if match2:
	        distance=int(match2.group(2))
		while(distance!=distance_last+1):
		    fpWrite.write("0\t")
		    k=k+1
		    distance=distance-1
                    if k>length-2:
                        break
                if k>length-2:
                    break
		fpWrite.write("%s\t" %match2.group(4))
		k=k+1
		distance_last=int(match2.group(2))
		other=other-int(match2.group(4))
#		print other
        if k<length-1:
	    for j in range (1,length-k):
	        fpWrite.write("0\t")
    	fpWrite.write("%d \n" %other)


    lines = fpRead.readline()

#print type(lines);
#while lines:
#    match = linePattern.match(lines)
#    if match:
#       print "I see you!" 
#       fpWrite.write("%s %s \n" %(match.group(3),match.group(5)))  
#    lines = fpRead.readline()
fpRead.close()
fpWrite.close()
