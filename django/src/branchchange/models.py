from django.db import models

# Create your models here.
class InitialForm(models.Model):
	username = models.CharField(max_length=100, blank=True, null=True)
	password = models.CharField(max_length=100, blank=True, null=True)

	def __unicode__(self):
		return self

class RegisterForm(models.Model):
	username = models.CharField(max_length=100, blank=True, null=True)
	password = models.CharField(max_length=100, blank=True, null=True)
	confirmpassword = models.CharField(max_length=100, blank=True, null=True)

	def __unicode__(self):
		return self

class BranchChangeForm(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	rollnumber= models.CharField(max_length=9, blank=True, null=True)
	currentdept= models.CharField(max_length=100, blank=True, null=True)
	cpi= models.DecimalField(max_digits=4, decimal_places=2)
	list_of_departments = (
		('CS', 'Computer Science'), ('EE', 'Electrical Engineering'), ('ME', 'Mechanical Engineering'), ('CE', 'Civil Engineering'), 
	)
	department = models.CharField(max_length=1, choices=list_of_departments, default='CS')
	def __unicode__(self):
		return self