from django import forms

from .models import InitialForm

class InitialFormSignup(forms.ModelForm):
	class Meta:
		model= InitialForm
		fields = ['username','password']