from django.contrib import admin
from django.urls import path 
from todolist import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.signup, name='signup'),
    path('signup/', views.signup, name='signup'),  
    path('login/', views.loginn, name='loginn'),
    path('todo/', views.todolis, name='todo')
]
