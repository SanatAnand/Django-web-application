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

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
