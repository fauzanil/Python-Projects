from loadcsv import *

print("========Bayessian classifier========")
print("========github.com/fauzanil=========")
filename = raw_input("Enter CSV File Name :")
length = int(raw_input("Enter CSV Length :"))
tuple = raw_input("Enter Tuple Test :")
print classFinder(classProbability(dataLister(length,filename),tuple))
