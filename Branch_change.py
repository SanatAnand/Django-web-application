import math
import csv
import sys


capacity = {}
strength = {}
original_strength = {}
students = []
waiting_list={}
outgoing_list={}

class Student:
        '''Class For the Students'''
        old_department = ''
        current_department = ''
        cpi = 0
        category = ''
        pref_list = []
        name = ''
        roll_number = ''
        def __init__(self,old_dept,curr_dept,given_cpi,cat,list_pref,given_name,given_roll_number):
                self.old_department = old_dept
                self.current_department = curr_dept
                self.cpi = given_cpi
                self.category = cat
                self.pref_list = list_pref
                self.name = given_name
                self.roll_number = given_roll_number

with open("input_programmes.csv") as inputfile :
	reader = csv.reader(inputfile)
	for rows in reader:
		capacity[rows[0]] = float(rows[1])
		strength[rows[0]] = float(rows[2])
                original_strength[rows[0]] = float(rows[2])
		waiting_list[rows[0]] = []
		outgoing_list[rows[0]] = []

with open("input_options.csv") as inputfile:
	reader = csv.reader(inputfile)
	for rows in reader:
		choices = []
		roll_number = rows[0]
		name = rows[1]
		dept = rows[2]
		cpi = float(rows[3])
                category = rows[4]        
		choices = (filter(None, rows[5:]))
		temporary_student = Student(dept,dept,cpi,category,choices,name,roll_number)
                if  ( category == 'GE' or category == 'OBC' ):
                        if cpi >= 8.0 :
                                students.append(temporary_student)
                else :
                        if cpi >= 7.0:
                                students.append(temporary_student)
                                
students.sort(key=lambda x: x.cpi, reverse=True)


for i in students:
	print i.old_department + " " + i.name + " " + str(i.cpi) + " " + i.category + " " + roll_number
	print i.pref_list
print len(students)

print "=================================================================="

def swap(s,s1):
	strength[s.current_department]-=1
	strength[s1]+=1
	s.current_department = s1
	temp_list = s.pref_list[:s.pref_list.index(s1)]
	s.pref_list = temp_list

def valid_shift(s,s1):
        if (strength[s.current_department] -1 >= round(0.75 * capacity[s.current_department]) ) and ( strength[s1] + 1 <= round(1.1 * capacity[s1]) ):
                return True
        return False

def check_waiting_list(dept):
        if waiting_list[dept] == []:
                return
        else :
                while waiting_list[dept] is not [] and valid_shift(waiting_list[dept][0],dept):
                        temp_dept = waiting_list[dept][0].current_department
                        swap(waiting_list[dept][0],dept)
                        temp_stu = waiting_list[dept][0]
                        waiting_list[dept] = waiting_list[dept][1:]
                        check_waiting_list(temp_dept)
                return

for stu in students:
        i=0
        while i< len(stu.pref_list) and not valid_shift(stu,stu.pref_list[i]):
                #print stu.name
                waiting_list[stu.pref_list[i]].append(stu)
                i +=1
        if i is not len(stu.pref_list):
                temp_department = stu.current_department
                swap(stu,stu.pref_list[i])
                check_waiting_list(temp_department)
        #print stu.name + ' ' + stu.old_department + ' ' + stu.current_department + ' '
        #print stu.pref_list

for i in students:
	print i.old_department + " " + i.name + " " + i.current_department + ' ' + str(i.cpi) + " " + i.category + " " + roll_number
	print i.pref_list
print len(students)

print "======================================================================="

for i in strength:
        print i + " " + str(original_strength[i]) + " " + str(strength[i])

#with open() as output_file:
#        writer=csv.writer
