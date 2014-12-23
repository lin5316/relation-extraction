from svmutil import *

y, x = svm_read_problem('train/feature.txt')
m = svm_train(y, x, '-c 4')
svm_save_model('relation_extraction.model', m)
