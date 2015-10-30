from django.db import models
from django.contrib import admin
from django.core.validators import MaxValueValidator
from 	django.core.validators import MinValueValidator
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
	cpi= models.DecimalField(max_digits=4, decimal_places=2, max_length=100, validators=[MinValueValidator(0.00),MaxValueValidator(10.00)])
	list_of_categories = (
		('A', 'GE'), ('B', 'OBC'), ('C', 'SC'), ('D', 'ST'), ('E', 'PwD')
	)

	list1=[]
	list2=[]

	with open("input_programmes.csv") as inputfile:
		reader = csv.reader(inputfile)
		j=0
		for rows in reader:
			j+=1
			list1.append(j)
			list2.append(rows[0])

	list_of_department_for_current = zip(list1,list2)
	list1.append(0)
	list2.append(None)
	list_of_departments = zip(list1,list2)
	
	category = models.CharField(max_length=1, choices=list_of_categories, default='A')
	department = models.IntegerField(choices=list_of_department_for_current, default=1)

	
	pref1 = models.IntegerField(choices=list_of_department_for_current, default=1)
	pref2 = models.IntegerField(choices=list_of_departments, default=0)
	pref3 = models.IntegerField(choices=list_of_departments, default=0)
	pref4 = models.IntegerField(choices=list_of_departments, default=0)
	pref5 = models.IntegerField(choices=list_of_departments, default=0)
	def __unicode__(self):
		return self.name

class BCAdmin(admin.ModelAdmin):
	actions = ['download_csv']
	def download_csv(self, request, queryset):

		list1=[]
		list2=[]
		
		import csv
		import os

		with open("input_programmes.csv") as inputfile:
			reader = csv.reader(inputfile)
			j=0
			for rows in reader:
				j+=1
				list1.append(j)
				list2.append(rows[0])
		list_of_departments = dict(zip(list1,list2))
		list_of_categories = {
			'A': 'GE', 'B': 'OBC', 'C': 'SC', 'D': 'ST', 
		}
		
		
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		output_file = open('input_options.csv', 'wb')
		writer = csv.writer(output_file)
		for s in queryset:
			s.department=list_of_departments[s.department]
			s.pref1=list_of_departments[s.pref1]
			if s.pref2!= 0:
				s.pref2=list_of_departments[s.pref2]
			if s.pref3!= 0:
				s.pref3=list_of_departments[s.pref3]
			if s.pref4!= 0:
				s.pref4=list_of_departments[s.pref4]
			if s.pref5!= 0:
				s.pref5=list_of_departments[s.pref5]
			
			s.category=list_of_categories[s.category]
			
			row = [s.rollnumber,s.name, s.department,  s.cpi, s.category,s.pref1]
			if s.pref2!=0:
				row.append(s.pref2)
			if s.pref3!= 0:
				row.append(s.pref3)
			if s.pref4!= 0:
				row.append(s.pref4)
			if s.pref5!= 0:
				row.append(s.pref5)

			writer.writerow(row)

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



admin.site.register(BranchChangeForm,BCAdmin)
admin.site.register(InputStudentPreferrenceList)
admin.site.register(InputBranchList)