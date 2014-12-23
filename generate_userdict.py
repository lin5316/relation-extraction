#encoding=utf-8

def from_test():
    input_file = open('test/data.txt','r')
    userdict = {}

    while (1):
        text = input_file.readline()
        if (text == ''):
            break

        while(1):
            line = input_file.readline()
            if (line == ''):
                break
            if (line == "|\n"):
                break

            entities = line.split(',')
            if len(entities) != 3:
                print 'broken entities: %s' % line
                continue
            if entities[2] == 'L\n':
                continue

            if entities[0] in userdict:
                times = userdict[entities[0]][0] + 1
                userdict[entities[0]] = (times, 'nr')
            else:
                userdict[entities[0]] = (1, 'nr')

            if entities[1] in userdict:
                times = userdict[entities[1]][0] + 1
                userdict[entities[1]] = (times, 'nt')
            else:
                userdict[entities[1]] = (1, 'nt')

    input_file.close()
    return userdict

def from_train(userdict):
    input_file = open('train/data.txt','r')

    while (1):
        text = input_file.readline()
        if (text == ''):
            break

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
                if nr[i] in userdict:
                    times = userdict[nr[i]][0] + 1
                    userdict[nr[i]] = (times, 'nr')
                else:
                    userdict[nr[i]] = (1, 'nr')

            for i in range(len(nt)):
                if nt[i] in userdict:
                    times = userdict[nt[i]][0] + 1
                    userdict[nt[i]] = (times, 'nt')
                else:
                    userdict[nt[i]] = (1, 'nt')

    input_file.close()
    return userdict

def correct_errors(userdict):
    correct_dict = {'nr':[],
                    'nt':[],
                    'ns':['嘉陵']}

    for e in correct_dict:
        l = correct_dict[e]
        for word in l:
            userdict[word] = (1000000, e)

    return userdict

if __name__ == '__main__':
    userdict = from_test()
    userdict = from_train(userdict)
    userdict = correct_errors(userdict)

    output_file = file('userdict.txt','w+')
    for word in sorted(userdict):
        output_file.write("%s %d %s\n" % (word, 1000000, userdict[word][1]))
    output_file.close()

