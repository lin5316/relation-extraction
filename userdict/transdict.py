import sys
import re

input_file = open("anjs_seg.dic")
output_file = file("transdict.txt","w+")

line = input_file.readline()
i = 0
while (line!=""):
	line = line.split("\t")
	line[2] = line[2].split("\n")
	if (line[1] == "nr") or (line[1] == "nt"):
		output_file.write(line[0])
		output_file.write(" ")
		output_file.write("1000000")#line[2][0]
		output_file.write(" ")
		output_file.write(line[1])
		output_file.write("\n")
	line = input_file.readline()

input_file.close()
output_file.close()
