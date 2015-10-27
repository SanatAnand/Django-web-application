from django.db import models

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
		('CS', 'Computer Science'), ('EE', 'Electrical Engineering'), ('ME', 'Mechanical Engineering'), ('CE', 'Civil Engineering'), 
	)
	list_of_categories = (
		('GE', 'GE'), ('OBC', 'OBC'), ('SC', 'SC'), ('ST', 'ST'), 
	)
	category = models.CharField(max_length=1, choices=list_of_categories, default='GE')
	department = models.CharField(max_length=1, choices=list_of_departments, default='CS')
	pref1=models.CharField(max_length=50, blank=True, null=True)
	pref2=models.CharField(max_length=50, blank=True, null=True)
	pref3=models.CharField(max_length=50, blank=True, null=True)
	pref4=models.CharField(max_length=50, blank=True, null=True)
	pref5=models.CharField(max_length=50, blank=True, null=True)
	def __unicode__(self):
		return self.name