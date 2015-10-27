from django.contrib import admin

# Register your models here.
from .models import InitialForm
from .models import RegisterForm
from .models import BranchChangeForm

class InitialFormAdmin(admin.ModelAdmin):
	class Meta:
		model=InitialForm

admin.site.register(InitialForm)
admin.site.register(RegisterForm)
#admin.site.register(BranchChangeForm)
