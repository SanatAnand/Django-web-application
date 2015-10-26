from django.shortcuts import render

from .forms import InitialFormSignup
# Create your views here.
def abc(request):
	topic= "BRANCH CHANGE"
	if request.method == "POST":
		print  request.POST
	form=InitialFormSignup(request.POST or None)
	context ={
		"xyz": topic,
		"form": form,
	}
	return render(request, "home.html",context)