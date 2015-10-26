from django import forms

from .models import InitialForm
from .models import RegisterForm
from .models import BranchChangeForm

class InitialFormSignup(forms.ModelForm):
	class Meta:
		model= InitialForm
		widgets = {
			'password': forms.PasswordInput(),
		}
		fields = ['username','password']


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
			raise forms.ValidationError('Username should not contain any space')
		#if username #is taken
		return name1
 

	def clean_password(self):
		password= self.cleaned_data.get('password')
		if ' ' in password:
			raise forms.ValidationError('Password should not contain any space')
		return password

	def clean_confirmpassword(self):
		confirmpassword= self.cleaned_data.get('confirmpassword')
		if password is not confirmpassword:
			raise forms.ValidationError("The passwords do not match")
		return confirmpassword

class BranchChangeFormSignup(forms.ModelForm):
	class Meta:
		model= BranchChangeForm
		widgets = {
			'password': forms.PasswordInput(),
		}
		fields = ['name','rollnumber','currentdept', 'cpi']