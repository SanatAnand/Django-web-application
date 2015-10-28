from django.contrib import admin

# Register your models here.
from .models import InitialForm
from .models import RegisterForm
from .models import BranchChangeForm
from .models import InputStudentPreferrenceList
from .models import BCAdmin
from .models import RunBranchAllotmentAlgorithm

class InitialFormAdmin(admin.ModelAdmin):
	class Meta:
		model=InitialForm

class BCAdminAdmin(admin.ModelAdmin):
	class Meta:
		model=BCAdmin

class RunBranchAllotmentAlgorithmAdmin(admin.ModelAdmin):
	class Meta:
		model=RunBranchAllotmentAlgorithm



admin.site.register(InitialForm)
admin.site.register(RegisterForm)
#admin.site.register(BranchChangeForm)
#admin.site.register(BranchChangeForm, BCAdminAdmin)
# admin.site.register(InputStudentPreferrenceList, RunBranchAllotmentAlgorithmAdmin)
