from django.shortcuts import render

from .forms import InitialFormSignup
from .forms import RegisterFormSignup

# Create your views here.
def homeview(request):
	topic= "BRANCH CHANGE"
	if request.method == "POST":
		print  request.POST
	form=InitialFormSignup(request.POST or None)

	context ={
		"xyz": topic,
		"form": form,
	}
	return render(request, "homepage.html",context)

def userloginview(request):
	topic= "USER LOGIN" 
	if request.method == "POST":
		print  request.POST
	form=InitialFormSignup(request.POST or None)

	context ={
		"xyz": topic,
		"form": form,
	}
	return render(request, "userlogin.html",context)

def adminloginview(request):
	topic= "ADMIN LOGIN" 
	if request.method == "POST":
		print  request.POST
	form=InitialFormSignup(request.POST or None)

	context ={
		"xyz": topic,
		"form": form,
	}
	return render(request, "adminlogin.html",context)

def registerview(request):
	topic= "REGISTER AS A NEW USER" 
	if request.method == "POST":
		print  request.POST
	form=RegisterFormSignup(request.POST or None)
	context ={
		"xyz": topic,
		"form": form,
	}
	return render(request, "register.html",context)