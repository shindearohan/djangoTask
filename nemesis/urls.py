from django.contrib import admin
from django.urls import path
from nemesis import views

urlpatterns = [
    path("", views.index, name='nemesis'),
    path('index', views.index, name='index'),
    path('user', views.user, name='user'),
    path('sign',views.sign, name='sign'),
    path('userdetails',views.userdetails, name='userdetails'),
    path('logoutuser',views.logoutuser, name='logoutuser'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('useredit',views.editrec, name='useredit'),
    path('editrec/<int:id>',views.editrec,name='editrec'),
    path('userdetails',views.editrec, name='edit'),
]