from svmutil import *

def predict():
    y, x = svm_read_problem('test/feature.txt')
    m = svm_load_model('relation_extraction.model')
    label, acc, val = svm_predict(y, x, m)
    return label

def save_result(label):
    record_file = open('test/record.txt','r')
    output_file = file('test/result.txt','w+')
    label_file = file('test/label.txt','w+')

    for i in range(len(label)):
        line = record_file.readline()
        label_file.write(str(label[i])+"\n")
        if label[i] == -1:
            continue
        output_file.write(line)
	
    record_file.close()
    output_file.close()
    label_file.close()

label = predict()
save_result(label)
