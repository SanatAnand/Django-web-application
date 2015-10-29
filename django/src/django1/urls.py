from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'branchchange.views.homeview', name='homeview'),
    url(r'^home/userlogin$', 'branchchange.views.userloginview', name='userloginview'),
    url(r'^home/adminlogin$', 'branchchange.views.adminloginview', name='adminloginview'),
    url(r'^home/register$', 'branchchange.views.registerview', name='registerview'),
    url(r'^home/userlogin/portal$', 'branchchange.views.branchchangeview', name='branchchangeview'),
    url(r'^home/adminlogin/loggedin$', 'branchchange.views.adminloggedinview', name='adminloggedinview'),
	url(r'^admin/branchchange/branchchangeform/run/$', 'branchchange.views.run_script', name='run_script'),
	url(r'^output_change_list$', 'branchchange.views.download_list_file', name='Download Final Branch Change List'),
	url(r'^output_list_stats$', 'branchchange.views.download_stats_file', name='Download Final Stats List'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
