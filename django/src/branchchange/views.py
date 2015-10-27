from django.shortcuts import render

from .forms import InitialFormSignup
from .forms import RegisterFormSignup
from .forms import BranchChangeFormSignup

# Create your views here.
def homeview(request):
	topic= "BRANCH CHANGE"
	#if request.method == "POST":
	#	print  request.POST
	form=InitialFormSignup(request.POST or None)

	context ={
		"xyz": topic,
		"form": form,
	}
	return render(request, "homepage.html",context)

def userloginview(request):
	topic= "USER LOGIN" 
	form=InitialFormSignup(request.POST or None)
	if request.method == "POST":
		print  request.POST
	context ={
		"xyz": topic,
		"form": form,
	}
	if request.method== "GET":
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
	form=RegisterFormSignup(request.POST or None)

	context ={
		"xyz": topic,
		"form": form,
	}	
	if request.method=="GET":
		print "see ya"
		return render(request, "register.html",context)

	if request.method == "POST":
		print "hiiiii"
		if form.is_valid():
			print "bye"
			instance= form.save(commit=False)
			username= form.cleaned_data.get("username")
			print username
			instance.save()
	

def branchchangeview(request):
	topic= "WELCOME TO BRANCH CHANGE PORTAL 2015 " 
	if request.method == "POST":
		print  request.POST
	form=BranchChangeFormSignup(request.POST or None)

	context ={
		"xyz": topic,
		"form": form,
	}
	return render(request, "userlogin.html",context)