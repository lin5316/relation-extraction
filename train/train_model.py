from svmutil import *

y, x = svm_read_problem('train/feature.txt')
#m = svm_train(y, x, '-c 4')
m = svm_train(y, x, '-s 0 -c 4 -w1 8 -w-1 1')
svm_save_model('relation_extraction.model', m)
