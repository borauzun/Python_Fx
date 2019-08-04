import csv
import Test3 as fl
import Test4 as fl2
with open('1.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for i,row in enumerate(reader):
        # print(row['survived'], row['pclass'], row['name'], row['sex'], row['age'])
        # print(fl.Add(float(row['open'])))
        fl2.printTest(row)
        if(i >= 9):break
