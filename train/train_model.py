from svmutil import *
import sys

def main(c):
    y, x = svm_read_problem('train/feature.txt')
    #m = svm_train(y, x, '-c 4')
    m = svm_train(y, x, '-s 0 -c %s' % c)# -w1 8 -w-1 1')
    svm_save_model('relation_extraction.model', m)

if len(sys.argv) > 1:
    main(sys.argv[1])
else:
    main()

