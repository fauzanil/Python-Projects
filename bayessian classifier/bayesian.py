from loadcsv import *

print("========Bayessian classifier========")
#print("========github.com/fauzanil=========")
filename = raw_input("Enter CSV File Name :")
length = int(raw_input("Enter CSV Column Length :"))
tupleraw = raw_input("Enter Tuple Test (With space without quote) :")
tuple = list(map(str, tupleraw.split()))
classified = classFinder(classProbability(dataLister(length,filename)[0],tuple))
print "Tuple classified as : " + classified
