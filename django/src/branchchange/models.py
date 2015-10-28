from django.db import models
from django.contrib import admin
import math
import csv
import sys
	
# Create your models here.
class InitialForm(models.Model):
	username = models.CharField(max_length=100, blank=True, null=True)
	password = models.CharField(max_length=100, blank=True, null=True)

	def __unicode__(self):
		return self.username

class RegisterForm(models.Model):
	username = models.CharField(max_length=100, blank=True, null=True)
	password = models.CharField(max_length=100, blank=True, null=True)
	confirmpassword = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return str(self.username)

class BranchChangeForm(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	rollnumber= models.CharField(max_length=9, blank=True, null=True)
	#currentdept= models.CharField(max_length=100, blank=True, null=True)
	cpi= models.DecimalField(max_digits=4, decimal_places=2, max_length=100)
	list_of_departments = (
		('A', 'Computer Science'), ('B', 'Electrical Engineering'), ('C', 'Mechanical Engineering'), ('D', 'Civil Engineering'), 
	)
	list_of_categories = (
		('A', 'GE'), ('B', 'OBC'), ('C', 'SC'), ('D', 'ST'), 
	)
	category = models.CharField(max_length=1, choices=list_of_categories, default='A')
	department = models.CharField(max_length=1, choices=list_of_departments, default='A')
	pref1=models.CharField(max_length=50, blank=True, null=True)
	pref2=models.CharField(max_length=50, blank=True, null=True)
	pref3=models.CharField(max_length=50, blank=True, null=True)
	pref4=models.CharField(max_length=50, blank=True, null=True)
	pref5=models.CharField(max_length=50, blank=True, null=True)
	def __unicode__(self):
		return self.name

class BCAdmin(admin.ModelAdmin):
	actions = ['download_csv']
	def download_csv(self, request, queryset):
		list_of_departments = {
		'A': 'Computer Science', 'B': 'Electrical Engineering', 'C': 'Mechanical Engineering', 'D': 'Civil Engineering', 
		}
		list_of_categories = {
			'A': 'GE', 'B': 'OBC', 'C': 'SC', 'D': 'ST', 
		}
		
		import csv
		import os
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		output_file = open('input_options.csv', 'wb')
		writer = csv.writer(output_file)
		for s in queryset:
			s.department=list_of_departments[s.department]
			s.category=list_of_categories[s.category]
			writer.writerow([s.rollnumber,s.name, s.department,  s.cpi, s.category,s.pref1,s.pref2,s.pref3,s.pref4,s.pref5])

	download_csv.short_description = "Download CSV file for selected stats."

class InputStudentPreferrenceList(models.Model):
	import os
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	#SAVE_DIR = os.path.dirname(BASE_DIR)
	input_file = models.FileField(upload_to=BASE_DIR)

	def __unicode__(self):
		return 'File'

class InputBranchList(models.Model):
	import os
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	#SAVE_DIR = os.path.dirname(BASE_DIR)
	input_file = models.FileField(upload_to=BASE_DIR)

	def __unicode__(self):
		return 'File'


class RunBranchAllotmentAlgorithm(admin.ModelAdmin):
	actions = ['run_script']
	def run_script(self,request,queryset):
		# import math
		# import csv
		# import sys

		changes = 1
		capacity = {}
		strength = {}
		original_strength = {}
		students = []
		cut_offs = {}
		final_matrix = []
		dept_matrix = []

		class Student:
			'''Class For the Students'''
			old_department = ''
			current_department = ''
			cpi = 0
			category = ''
			pref_list = []
			name = ''
			roll_number = ''
			present = None
			eligible = None
			def __init__(self,old_dept,curr_dept,given_cpi,cat,list_pref,given_name,given_roll_number):
				self.old_department = old_dept
				self.current_department = curr_dept
				self.cpi = given_cpi
				self.category = cat
				self.pref_list = list_pref
				self.name = given_name
				self.roll_number = given_roll_number
				self.present = True
				self.eligible = True

		with open("input_programmes.csv") as inputfile :
			reader = csv.reader(inputfile)
			for rows in reader:
				capacity[rows[0]] = float(rows[1])
				strength[rows[0]] = float(rows[2])
				original_strength[rows[0]] = float(rows[2])
				cut_offs[rows[0]] = float(11)
				#waiting_list[rows[0]] = []
				#outgoing_list[rows[0]] = []

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
					else:
						temporary_student.eligible = False
						students.append(temporary_student)
				else :
					if cpi >= 7.0:
						students.append(temporary_student)
					else:
						temporary_student.eligible = False
						students.append(temporary_student)


		students.sort(key=lambda x: x.cpi, reverse=True)


		# for i in students:
		# 	print i.old_department + " " + i.name + " " + str(i.cpi) + " " + i.category + " " + roll_number
		# 	print i.pref_list
		# print len(students)

		print cut_offs

		print "=================================================================="

		def swap(s,s1):
			strength[s.current_department]-=1
			strength[s1]+=1
			s.current_department = s1
			temp_list = s.pref_list[:s.pref_list.index(s1)]
			s.pref_list = temp_list
			cut_offs[s1] = min(float(s.cpi),cut_offs[s1])

		def valid_shift(s,s1):
				if (strength[s.current_department] -1 >= round(0.75 * capacity[s.current_department]) ) and ( strength[s1] + 1 <= round(1.1 * capacity[s1]) ):
					return True
				if s.cpi >= 9 and ( strength[s1] + 1 <= round(1.1 * capacity[s1]) ):
					return True
				if s.cpi == cut_offs[s1]:
					return True
				return False

		# def check_waiting_list(dept):
		#         if waiting_list[dept] == []:
		#                 return
		#         else :
		#                 while waiting_list[dept] is not [] and valid_shift(waiting_list[dept][0],dept):
		#                         temp_dept = waiting_list[dept][0].current_department
		#                         swap(waiting_list[dept][0],dept)
		#                         temp_stu = waiting_list[dept][0]
		#                         waiting_list[dept] = waiting_list[dept][1:]
		#                         check_waiting_list(temp_dept)
		#                 return

		# def check_outgoing_list(dept):
		#         if outgoing_list[dept] == []:
		#                 return
		#         else :
		#                 while outgoing_list[dept] is not [] and valid_shift(outgoing_list[dept][0],dept):
		#                         temp_dept = waiting_list[dept][0].current_department
		#                         swap(waiting_list[dept][0],dept)
		#                         temp_stu = waiting_list[dept][0]
		#                         waiting_list[dept] = waiting_list[dept][1:]
		#                         check_waiting_list(temp_dept)
		#                 return

		while changes is not 0 and students is not []:
				changes = 0
				#print valid_shift(students[0],students[0].pref_list[0])
				for stu in students:
					if stu.present and stu.eligible:
						i=0
						if valid_shift(stu,stu.pref_list[0]):
							print stu.name
							swap(stu,stu.pref_list[0])
							changes += 1
							stu.present = False
						while i< len(stu.pref_list) and not valid_shift(stu,stu.pref_list[i]):
								i +=1
						if i is not len(stu.pref_list):
								swap(stu,stu.pref_list[i])
								changes += 1
				print "========================================================================"
				print cut_offs
				print "========================================================================"



		# for stu in students:
		#         i=0
		#         while i< len(stu.pref_list) and not valid_shift(stu,stu.pref_list[i]):
		#                 #print stu.name
		#                 waiting_list[stu.pref_list[i]].append(stu)
		#                 i +=1
		#         if i is not len(stu.pref_list):
		#                 temp_department = stu.current_department
		#                 swap(stu,stu.pref_list[i])
		#                 check_waiting_list(temp_department)
		#         outgoing_list[stu.current_department].append(stu)
		#         #print stu.name + ' ' + stu.old_department + ' ' + stu.current_department + ' '
		#         #print stu.pref_list

		for i in students:
			print i.old_department + " " + i.name + " " + i.current_department + ' ' + str(i.cpi) + " " + i.category + " " + roll_number
			print i.pref_list
		print len(students)

		print "======================================================================="

		for i in strength:
			print i + " " + str(original_strength[i]) + " " + str(strength[i])
		dept_matrix.append(["Program", "Cutoff","Santioned Strength","Original Strength","Final Strength"])
		for dep in cut_offs:
			if(int(cut_offs[dep]) is int(11)):
				dept_matrix.append([dep,"NA",capacity[dep],original_strength[dep],strength[dep]])
			else:
				dept_matrix.append([dep,cut_offs[dep],capacity[dep],original_strength[dep],strength[dep]])

		for stu in students:
			if stu.old_department == stu.current_department:
				stu.current_department = "Branch Unchanged"
			if stu.eligible is False:
				stu.current_department = "Ineligible"
			final_matrix.append([stu.roll_number,stu.name,stu.old_department,stu.current_department])

		final_matrix.sort(key=lambda x: (x[0], x[1].lower(),x[2]))
		with open('stats.csv','wb') as output_file:
			writer = csv.writer(output_file, delimiter=',')
			writer.writerows(dept_matrix)

		with open('output.csv', 'wb') as output_file:
				writer = csv.writer(output_file, delimiter=',')
				writer.writerows(final_matrix)
				pass

admin.site.register(BranchChangeForm,BCAdmin)
admin.site.register(InputStudentPreferrenceList, RunBranchAllotmentAlgorithm)
admin.site.register(InputBranchList)