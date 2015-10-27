import csv
from django.shortcuts import render
from django.shortcuts import redirect

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

####################################################################### USER LOGIN

def userloginview(request):
	topic = "LOGIN AS USER"
	if request.method == 'POST':
		form = InitialFormSignup(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			return redirect('branchchange.views.branchchangeview')
	else:
		form = InitialFormSignup()

	context ={
		"xyz": topic,
		"form": form,
	}
	return render(request,'userlogin.html', context)

####################################################################### ADMIN LOGIN

def adminloginview(request):
	topic = "LOGIN AS ADMIN"
	if request.method == 'POST':
		form = InitialFormSignup(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			if instance.username == "admin" and instance.password=="admin123":
				print instance.username
				print instance.password
				return redirect('branchchange.views.adminloggedinview')
			else:
				return redirect('branchchange.views.adminloginview')
	else:
		form = InitialFormSignup()

	context ={
		"xyz": topic,
		"form": form,
	}
	return render(request,'adminlogin.html', context)

############################################################################ REGISTER USER

def registerview(request):
	topic= "REGISTER AS A NEW USER" 
	if request.method == 'POST':
		form = RegisterFormSignup(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			return redirect('branchchange.views.homeview')
	else:
		form = RegisterFormSignup()

	context ={
		"xyz": topic,
		"form": form,
	}
	return render(request,'register.html', context)

########################################################################### BRANCH CHANGE APPLICATION FORM

def branchchangeview(request):
	topic= "APPLICATION FOR BRANCH CHANGE 2016" 
	if request.method == 'POST':
		form = BranchChangeFormSignup(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			return redirect('branchchange.views.homeview')
	else:
		form = BranchChangeFormSignup()

	context ={
		"xyz": topic,
		"form": form,
	}
	return render(request,'branchchangeform.html', context)

############################################################################# AFTER ADMIN LOGS IN

def adminloggedinview(request):
	topic= "WELCOME ADMIN" 
	#if request.method == "POST":
	#	print  request.POST
	form=InitialFormSignup(request.POST or None)

	context ={
		"xyz": topic,
		"form": form,
	}
	return render(request, "adminpage.html",context)

############################################################################# CREATE CSV
	
# def export(fields=None):
# 	queryset = BranchChangeForm.objects.all()
# 	model = qs.model
# 	response = HttpResponse(mimetype='text/csv')
# 	response['Content-Disposition'] = 'attachment; filename=input_options.csv')
# 	writer = csv.writer(response)
# 	for obj in qs:
# 		row = []
# 		for field in headers:
# 			if field in headers:
# 				val = getattr(obj, field)
# 				if callable(val):
# 					val = val()
# 					row.append(val)
# 					writer.writerow(row)
# 	# Return CSV file to browser as download
# 	return response