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



admin.site.register(BranchChangeForm,BCAdmin)
admin.site.register(InputStudentPreferrenceList)
admin.site.register(InputBranchList)