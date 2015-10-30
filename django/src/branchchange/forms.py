from django import forms
#from django.shortcuts import get_object

from .models import InitialForm
from .models import RegisterForm
from .models import BranchChangeForm
#from .models import InputStudentPreferrenceList


class InitialFormSignup(forms.ModelForm):
	user = ''
	passw = ''

	class Meta:
		model= InitialForm
		widgets = {
			'password': forms.PasswordInput(),
		}
		fields = ['username','password']

	def clean_username(self):
		username= self.cleaned_data.get('username')
		#print username
		if ' ' in username:
			raise forms.ValidationError('Username should not contain any spaces')
		#if username #is taken
		return username

	def clean_password(self):
		password= self.cleaned_data.get('password')
		if ' ' in password:
			raise forms.ValidationError('Password should not contain any spaces')
		username= self.cleaned_data.get('username')
		#user = get_object(RegisterForm, username=username)
		q= RegisterForm.objects.all().filter(username=username)
		if not q.exists():
			raise forms.ValidationError('Plese Enter a valid username')
		else:
			user = q[0]
		passw = user.password
		if passw == password:
			return password
		else:
			raise forms.ValidationError('Wrong Password')
		

class RegisterFormSignup(forms.ModelForm):
	class Meta:
		model= RegisterForm
		widgets = {
			'password': forms.PasswordInput(),
			'confirmpassword': forms.PasswordInput(),
		}
		fields = ['username','password', 'confirmpassword']

	def clean_username(self):
		username= self.cleaned_data.get('username')
		#print username
		if ' ' in username:
			raise forms.ValidationError('Username should not contain any spaces')
		#if username #is taken
		q= RegisterForm.objects.all().filter(username=username)
		if q.exists():
			raise forms.ValidationError('Already a registered user. Try another username')
		return username

	def clean_password(self):
		password= self.cleaned_data.get('password')
		if ' ' in password:
			raise forms.ValidationError('Password should not contain any spaces')
		return password

	def clean_confirmpassword(self):
		password= self.cleaned_data.get('password')
		confirmpassword= self.cleaned_data.get('confirmpassword')
		#print password
		#print confirmpassword
		if password == confirmpassword:
			#print 'yo'
			return confirmpassword
		else:
			#print 'yo2'
			raise forms.ValidationError("The passwords do not match")

class BranchChangeFormSignup(forms.ModelForm):
	class Meta:
		model= BranchChangeForm
		widgets = {
			'password': forms.PasswordInput(),
		}
		fields = ['name','rollnumber','cpi','department','category','pref1','pref2','pref3','pref4','pref5']

	def clean_rollnumber(self):
		rollnumber= self.cleaned_data.get('rollnumber')
		if ' ' in rollnumber:
			raise forms.ValidationError('Invalid Roll Number')
		if '15' in rollnumber:
			return rollnumber
		else:
			raise forms.ValidationError('Invalid Roll Number')

	def clean_cpi(self):
		cpi= self.cleaned_data.get('cpi')
		if cpi > 10.00 :
			raise forms.ValidationError('Invalid CPI')
		if cpi < 0.00 :
			raise forms.ValidationError('Invalid CPI')
		return cpi

	def clean_pref1(self):
		department= self.cleaned_data.get('department')
		pref1= self.cleaned_data.get('pref1')
		if pref1 is department:
			raise forms.ValidationError('Cannot change to your original branch')	
		return pref1

	def clean_pref2(self):
		department= self.cleaned_data.get('department')
		pref1= self.cleaned_data.get('pref1')
		pref2= self.cleaned_data.get('pref2')
		if (pref2 is department) or (pref2 is pref1):
			raise forms.ValidationError('Choose a valid department')	
		return pref2

	def clean_pref3(self):
		department= self.cleaned_data.get('department')
		pref1= self.cleaned_data.get('pref1')
		pref2= self.cleaned_data.get('pref2')
		pref3= self.cleaned_data.get('pref3')
		if pref3 is not 0:
			if (pref3 is department) or (pref3 is pref1) or (pref3 is pref2):
				raise forms.ValidationError('Choose a valid department')	
			if pref2 is 0:
				raise forms.ValidationError('First enter a higher preference')
		return pref3

	def clean_pref4(self):
		department= self.cleaned_data.get('department')
		pref1= self.cleaned_data.get('pref1')
		pref2= self.cleaned_data.get('pref2')
		pref3= self.cleaned_data.get('pref3')
		pref4= self.cleaned_data.get('pref4')
		if pref4 is not 0:
			if (pref4 is department) or (pref4 is pref1) or (pref4 is pref2) or (pref4 is pref3):
				raise forms.ValidationError('Choose a valid department')	
			if (pref3 is 0) or (pref2 is 0):
				raise forms.ValidationError('First enter a higher preference')
		return pref4

	def clean_pref5(self):
		department= self.cleaned_data.get('department')
		pref1= self.cleaned_data.get('pref1')
		pref2= self.cleaned_data.get('pref2')
		pref3= self.cleaned_data.get('pref3')
		pref4= self.cleaned_data.get('pref4')
		pref5= self.cleaned_data.get('pref5')
		if pref5 is not 0:
			if (pref5 is department) or (pref5 is pref1) or (pref5 is pref2) or (pref5 is pref3) or (pref5 is pref4):
				raise forms.ValidationError('Choose a valid department')	
			if (pref3 is 0) or (pref2 is 0) or (pref4 is 0):
				raise forms.ValidationError('First enter a higher preference')
		return pref5
