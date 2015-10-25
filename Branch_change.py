import csv
import sys

capacity = {}
occupancy = {}
dept = []
name = []
cpi = []
catg = []
choices = []
students = []
		

with open("input_programmes.csv") as inputfile :
	reader = csv.reader(inputfile)
	for rows in reader:
		capacity[rows[0]] = rows[1]
		occupancy[rows[0]] = rows[2]

with open("input_options.csv") as inputfile:
	reader = csv.reader(inputfile)
	for rows in reader:
		students.append(rows[1])
		dept.append(rows[2])
		name.append(rows[0])
		cpi.append(rows[3])
		catg.append(rows[4])
		choices.append(filter(None, rows[5:]))

#students.sort(key=.get)
print students
X = students
Y = cpi
keydict = dict(zip(X, Y))
X.sort(key=keydict.get)
#for i in range(len(students)):
#	print name[i] + " " + dept[i] + " " + str(cpi[i]) + " " + catg[i]
#	print choices[i]
print X
