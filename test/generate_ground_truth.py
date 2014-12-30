import sys
sys.path.append('.')

from feature_generator import feature_generator

if __name__ == '__main__':
    input_file = open('test/data.txt','r')
    output_file = file('test/ground_truth.txt','w+')

    fg = feature_generator()
    cursor = 0
    while (1):
        cursor += 1
        text = input_file.readline()
        if (text == ''):
            break

        nrs = []
        nts = []
        while(1):
            line = input_file.readline()
            if (line == ''):
                break
            if (line == "|\n"):
                break

            entities = line.split(',')
            if len(entities) != 3:
                print "broken labelled entities: %s" % line
                continue

            nr = entities[0]
            nt = entities[1]
            relation = entities[2]

            if (relation=="L\n"):
                continue
            nrs.append(nr)
            nts.append(nt)

        for i in range (len(nrs)):
            output_file.write("%d %s %s\n" % (cursor, nrs[i], nts[i]))

    output_file.close()
    input_file.close()
