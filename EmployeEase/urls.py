"""EmployeEase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from Employe import views
urlpatterns = [

    url(r'^accounts/', include('django.contrib.auth.urls'), {"template_name": "login.html"}),
    url(r'^register/',views.register,name="register"),

    url(r'^admin/', admin.site.urls),
    url(r'^jobs/(?P<location>[A-Za-z].*)/(?P<sector>[A-Za-z].*)/(?P<range>[0-9].*)',login_required(views.get_jobs.as_view()),name="job"),
    url(r'^add/',login_required(views.add_job.as_view()),name="addJob"),
    url(r'^auth/',views.signuplogin,name="sl"),
    url(r'^about/(?P<jobid>[0-9]*)',views.get_description,name="desc"),
    url(r'^jobs/get/(?P<search>[A-Za-z]*)',views.get_jobs_list,name="backend"),
    url(r'^ack/(?P<stats>[A-Za-z]*)',views.status,name="finale"),
    url(r'^$',views.search_job.as_view(),name="index")
]