__author__ = 'ankit'


import string

import time
import csv

monthMap = []


def sharesOfTheDay(filename, inMonth):
    sum = 0
    activity = file(filename, 'rU')
    read = csv.DictReader(activity)
    for row in read:
        for items in row.items():
            if items[1].split('|')[3] < "12:00:00":

                inMonth[items[1].split('|')[1]] = inMonth.get(items[1].split('|')[1], 0) + int(items[1].split('|')[5])

            else:
                return

                #print items[1]


def main():
    list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sum = 0

    for month in range(1, 13):
        inMonth = {}
        for day in range(1, 32):
            start = time.clock()
            try:
                print "before"
                file_name = "./" + list[month - 1] + "/2013" + str(month).zfill(2) + str(day).zfill(2) + ".trd"
                print file_name
                sharesOfTheDay(file_name, inMonth)
            except Exception:
                # print "ExceptionOccured"
                noUseVariable = 0
            finish = time.clock()
            print finish - start
            print monthMap
            print inMonth
        monthMap.append(inMonth)


    i = 1
    dataset = []
    row = ["Month", "CompanyName", "NumOfShares"]
    dataset.append(row)

    for each in monthMap:

        for key, value in each.iteritems():
            row = []
            row.append(str(i))
            row.append(key)
            row.append(value)
            dataset.append(row)

        i += 1
    with open('TrustDataset.csv', 'wb') as fp:
        a = csv.writer(fp, delimiter=',')
        print dataset
        a.writerows(dataset)



if __name__ == '__main__':
    main()
