from django import forms
from django.shortcuts import get_object_or_404

from .models import InitialForm
from .models import RegisterForm
from .models import BranchChangeForm


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
		user = get_object_or_404(RegisterForm, username=username)
		passw = user.password
		if passw == password:
			return password
		else:
			raise forms.ValidationError('Invalid Login Credentials')
		

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

	

