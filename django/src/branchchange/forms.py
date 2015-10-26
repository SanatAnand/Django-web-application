from django import forms

from .models import InitialForm
from .models import RegisterForm

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