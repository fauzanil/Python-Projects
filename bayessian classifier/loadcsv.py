import csv


def dataLister(labelRange,inputCSV,):
    with open(inputCSV,"rb") as f:
        included_cols = [i for i in range (0,labelRange)]
        content = []
        reader = csv.reader(f)
        for row in reader:
            content.append(list(row[i] for i in included_cols))
        return content



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

    #return result,classProb,sum-1
    #return (len(tuples))

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






