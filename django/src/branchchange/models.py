from django.db import models
from django.contrib import admin

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
	actions = ['download_csv', 'import_csv']
	def download_csv(self, request, queryset):
		import csv
		output_file = open('output.csv', 'wb')
		writer = csv.writer(output_file)
		for s in queryset:
			writer.writerow([s.name, s.rollnumber, s.cpi, s.department,s.category,s.pref1,s.pref2,s.pref3,s.pref4,s.pref5])
	download_csv.short_description = "Download CSV file for selected stats."

class InputStudentPreferrenceList(models.Model):
	input_file = models.FileField()#upload_to='/branchchange')

	def __unicode__(self):
		return 'File'


	# def import_csv(self,request, queryset):
	# 	# Full path and name to your csv file
	# 	csv_filepathname="input_programmes.csv"
	# 	import sys,os,csv
	# 	dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
	# 	for row in dataReader:
	# 		branchchangeentry = BranchChangeForm()
	# 		branchchangeentry.name = row[1]
	# 		branchchangeentry.rollnumber = row[0]
	# 		branchchangeentry.department = row[2]
	# 		branchchangeentry.cpi = row[3]
	# 		branchchangeentry.category = rows[4]
	# 		branchchangeentry.prefs1 = rows[5]

admin.site.register(BranchChangeForm,BCAdmin)