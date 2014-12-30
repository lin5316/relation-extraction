import sys
sys.path.append('.')

import re
from feature_generator import feature_generator

def main(num_neighbors = 3, neg_rate = 100):
    input_file = open('train/data.txt','r')
    output_file = file('train/feature.txt','w+')
    fg = feature_generator()
    fg.set_num_neighbors(num_neighbors)
    fg.set_neg_rate(neg_rate)

    while (1):
        line_content = input_file.readline()
        if (line_content == ''):
            break

        nrs = []
        nts = []
        while(1):
            line = input_file.readline()
            if (line == ''):
                break
            if (line == "\n"):
                break
            nr_nt = line.split("|")
            nr = nr_nt[0].split(",")
            nt = nr_nt[1].split(",")
            for i in range(len(nr)):
                for j in range(len(nt)):
                    nrs.append(nr[i])
                    nts.append(nt[j])

        text = re.sub(r'[\{|/ns\}|/nt\}|/nr\}]','',line_content)
        output_file.write(fg.get_feature_strs(text, nrs, nts))

    output_file.close()
    input_file.close()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(eval(sys.argv[1]))
    elif len(sys.argv) == 3:
        main(eval(sys.argv[1]), eval(sys.argv[2]))
    else:
        main()
