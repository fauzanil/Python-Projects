#Filename :bayessian.py
#----------------Simple Bayessian Classifier------------------
#---------Fauzanil Zaki, Wiladhianty Yulianova 2016-----------
#------------------github.com/fauzanil------------------------
# Version 1.1
# Main file for bayessian classifier
# Continous data is not supported yet

from loadcsv import *

print("========Bayessian classifier========")
filename = raw_input("Enter CSV File Name :")
length = int(raw_input("Enter CSV Column Length :"))
tupleraw = raw_input("Enter Tuple Test (With space without quote) :")
tuple = list(map(str, tupleraw.split()))
if(len(tuple) != (length) - 1):
    print("Tuple size not match, it should be " +str(length -1)+(" tuple"))
else:
    classified = classFinder(classProbability(dataLister(length,filename),tuple))
    print ("Tuple classified as : " + classified)
    raw_input("Press Enter to continue...")