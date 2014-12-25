import sys

fs = open('train/feature.txt','r')
output_file = file('train/feature_stat.txt','w+')
lines = fs.readlines()
pos = 0
nag = 0
for line in lines:
	if line[0] == '-':
		nag = nag + 1
	else:
		pos = pos + 1
output_file.write(str(pos)+"\n")
output_file.write(str(nag)+"\n")
output_file.close()
