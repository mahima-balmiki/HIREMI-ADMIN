from django.contrib import admin
from django.urls import path
from dashboard import views

urlpatterns = [
     path("",views.index,name='index'),
     path("signup",views.signup,name='signup'),
     path("signin",views.signin,name='signin'),
     path("dashboard",views.dashboard,name='dashboard'),
     path("internship",views.internship,name='internship'),
     path("fresher",views.fresher,name='fresher'),
     path("experience",views.experience,name='experience'),
     path("mentorship",views.mentorship,name='mentorship'),
     path("training",views.training,name='training'),
     path("corporate",views.corporate,name='corporate'),
]
