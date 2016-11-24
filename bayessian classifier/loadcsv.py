#Filename :loadcsv.py
#----------------Simple Bayessian Classifier------------------
#---------Fauzanil Zaki, Wiladhianty Yulianova 2016-----------
#------------------github.com/fauzanil------------------------
#contain functions that used

#library Load
import csv


#Func           : dataLister put the csv into formatable list
#Input          : CSV lable range, CSV file name
#Return Value   : Listed data, data length

def dataLister(labelRange,inputCSV,):
    with open(inputCSV,"rb") as f:
        included_cols = [i for i in range (0,labelRange)]
        content = []
        reader = csv.reader(f)
        for row in reader:
            content.append(list(row[i] for i in included_cols))
        return content


#Func           : classProbability find class probavility and probability for each tuple
#Input          : listedData, Tuples
#Return Value   : Class probability, and each tuple probability in dictionary format for each tuple


def classProbability(listedData,tuples):
    result = {}
    classProb = {}
    tupleProb = {}
    structure = {}
    sum = 0
    for data in listedData:
        sum += 1
        if ((data[len(data) - 1]) not in listedData[0]):
            if (data[len(data) - 1] in result):
                result[data[len(data) - 1]] += 1
            else:
                result[data[len(data) - 1]] = 1
    for key in result:
        classProb[key] = (result.get(key)/float(sum-1))

    j=0
    n = 0
    while (j < len(tuples)):
        tupleProb[n] = {}
        for i in range(1, len(listedData)):
            if(tuples[j] == listedData[i][j]):
                if(listedData[i][6] in tupleProb[n]):
                    tupleProb[n][listedData[i][len(tuples)]] += 1
                else:
                    tupleProb[n][listedData[i][len(tuples)]] = 1
        j+=1
        n+=1

    for keynum in tupleProb:
        for keyclass in tupleProb[keynum]:
            tupleProb[keynum][keyclass] = float(tupleProb[keynum][keyclass]) / float(result[keyclass])



    return tupleProb,result




#Func           : classFinder find class for tuple
#Input          : data (dictionary whlist list every probability for each class available)
# ex {0:{class1 : value},{class2:value}}
#Return Value   : Classified class



def classFinder(data):
    classes = {}
    max = 0
    classResult = ""
    for keynum in data[0]:
        for keyclass in data[0][keynum]:
            classes[keyclass] = 1

    for keynum in data[0]:
        for keyclass in data[0][keynum]:
            classes[keyclass] = classes[keyclass] * data[0][keynum][keyclass]

    for key in classes:
        if (classes[key] > max):
            max = classes[key]
            classResult = key

    return classResult







