from svmutil import *

def predict():
    y, x = svm_read_problem('test/feature.txt')
    m = svm_load_model('relation_extraction.model')
    label, acc, val = svm_predict(y, x, m)
    return label, val

def save_result(label, val):
    record_file = open('test/record.txt','r')
    output_file = file('test/result.txt','w+')
    label_file = file('test/label.txt','w+')

    for i in range(len(label)):
        line = record_file.readline()
        label_file.write("%d %f\n" % (label[i], val[i][0]))
        if val[i][0] >= -0.2:
            continue
        output_file.write(line)

    record_file.close()
    output_file.close()
    label_file.close()

label, val = predict()
save_result(label, val)
