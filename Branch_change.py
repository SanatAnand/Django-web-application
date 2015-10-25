import csv
import sys

capacity = {}
strength = {}
students = []

class Student:
        '''Class For the Students'''
        old_department = ''
        current_department = ''
        cpi = 0
        pref_list = []
        name = ''
        roll_number = ''
        def __init__(self,old_dept,curr_dept,given_cpi,list_pref,given_name,given_roll_number):
                self.old_department = old_dept
                self.current_department = curr_dept
                self.cpi = given_cpi
                self.pref_list = list_pref
                self.name = given_name
                self.roll_number = given_roll_number

with open("input_programmes.csv") as inputfile :
	reader = csv.reader(inputfile)
	for rows in reader:
		capacity[rows[0]] = rows[1]
		strength[rows[0]] = rows[2]

with open("input_options.csv") as inputfile:
	reader = csv.reader(inputfile)
	for rows in reader:
                choices = []
		roll_number = rows[0]
		name = rows[1]
		dept = rows[2]
		cpi = rows[3]
        	choices.append(filter(None, rows[5:]))
                temporary_student = Student(dept,dept,cpi,choices,name,roll_number)
                students.append(temporary_student)

#students.sort(key=.get)
#print students
#X = students
#Y = cpi
#keydict = dict(zip(X, Y))
#X.sort(key=keydict.get)
#for i in range(len(students)):
#	print name[i] + " " + dept[i] + " " + str(cpi[i]) + " " + catg[i]
#	print choices[i]
#print X
