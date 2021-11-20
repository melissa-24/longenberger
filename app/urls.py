from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('logReg/', views.logReg),
    path('login/', views.login),
    path('register/', views.register),
    path('dashboard/', views.adminDash),
    path('logout/', views.logout),
    path('theAdmin/createPage/', views.createPage),
    path('theAdmin/createType/', views.createType),
    path('theAdmin/createTopic/', views.createTopic),
    path('theAdmin/createLink/', views.createLink),
]