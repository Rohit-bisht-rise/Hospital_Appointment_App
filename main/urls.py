from . import views
from django.urls import path

urlpatterns = [
    path('', views.homePage, name='home'),
    path('patient/', views.patientPage, name="patient"),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
]
