__author__ = 'ankit'

#graph is saved as temp.png
from matplotlib import pyplot as plt
import plotly
import csv

def companyGraph(companyName):
    filename="TrustDataset.csv"
    activity = file(filename, 'rU')
    read = csv.DictReader(activity)
    shareList=[]
    for row in read:
        if row['CompanyName']==companyName:
            shareList.append(int(row['NumOfShares']))

    monthList=[1,2,3,4,5,6,7,8,9,10,11,12]
    plt.plot(monthList,shareList,"ro")
    plt.plot(monthList,shareList)





def main():
    plt.xlabel("Months")
    plt.ylabel("Shares")
    plt.title("Year:2013")
    list=["BANKINDIA"] #update this list with the names of the companies for which you want to plot.
    try:
        for each in list:
            companyGraph(each)
        #print row
    except Exception:
        noUseVariable=0
        #print "ExceptionOccured"


    plt.savefig("temp.png")
    plt.show()


if __name__ == '__main__':
    main()

