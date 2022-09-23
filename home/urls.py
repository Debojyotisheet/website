from django.contrib import admin
from django.urls import path
from home import views

#  Admin panel customization 
admin.site.site_header="Login to Dedpool's Dashboard"
admin.site.site_title="Weldome to the dashboard"
admin.site.index_title="Welcome to the potarl"
urlpatterns = [
    path('',views.page,name="page"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('projects',views.projects,name="projects")
]