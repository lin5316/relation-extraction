import sys
sys.path.append('.')

from feature_generator import feature_generator

def main(num_neighbors = 3):
    input_file = open('test/data.txt','r')
    output_file = file('test/feature.txt','w+')
    output_xml = file('test/record.txt', 'w+')

    fg = feature_generator()
    fg.set_num_neighbors(num_neighbors)
    cursor = 0
    while (1):
        cursor += 1
        text = input_file.readline()
        if (text == ''):
            break

        while(1):
            line = input_file.readline()
            if (line == ''):
                break
            if (line == "|\n"):
                break

        feature_strs, entity_strs = fg.get_feature_entity_strs(text)
        output_file.write(feature_strs)

        entities = entity_strs.split('\n')
        for entity in entities:
            if entity == '':
                continue
            output_xml.write("%d %s\n" % (cursor, entity))

    output_file.close()
    input_file.close()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(eval(sys.argv[1]))
    else:
        main()
