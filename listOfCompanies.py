__author__ = 'ankit'
import string

import time
import csv

def main():
    filename="TrustDataset.csv"
    activity = file(filename, 'rU')
    read = csv.DictReader(activity)
    dictionary={}
    for row in read:
        dictionary[row['CompanyName']]=dictionary.get(row['CompanyName'],0)+1
    dataset=[]
    dataset.append(["CompanyName"])
    for key,value in dictionary.iteritems():

            if value==12:
                list=[]
                list.append(key)
                dataset.append(list)
    dataset.sort()
    with open('ListOFCompanies.csv', 'wb') as fp:
        a = csv.writer(fp, delimiter=',')
        print dataset
        a.writerows(dataset)





if __name__ == '__main__':
    main()
