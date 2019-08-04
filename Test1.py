import csv
import 'Test3.py' as fl
total, survived = 0, 0

with open('1.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for i,row in enumerate(reader):
        # print(row['survived'], row['pclass'], row['name'], row['sex'], row['age'])
        total+= 1
        if(float(row['open'])<1.25): survived+=1
        #if(i >= 9):break
print('total: {}, survived: {} ({:.2f}%)'.format(total, survived,
                                                 survived/total * 100))
