
from django.urls import path
from . import views

urlpatterns = [
    path("", views.landingPage, name="landingPage"),
    path('loginPage/', views.loginPage, name='loginPage'),
    path('signUpPage/', views.signUpPage, name='signUpPage'),
    path('dashboardPage/', views.dashboardPage, name='dashboardPage'),
    path('calendarPage/', views.calendarPage, name='calendarPage'),
    path('workoutRoutinePage/', views.workoutRoutinePage, name='workoutRoutinePage'), 
    path('prsPage/', views.prsPage, name='prsPage'),
    path('exploreWorkoutsPage/', views.exploreWorkoutsPage, name='exploreWorkoutsPage')
]