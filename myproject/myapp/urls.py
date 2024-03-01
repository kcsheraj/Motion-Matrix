
from django.urls import path
from . import views

urlpatterns = [
    path("", views.landingPage, name="landingPage"),
    path('loginPage/', views.loginPage, name='loginPage'),
    path('dashboardPage/', views.dashboardPage, name='dashboardPage'),
    path('calenderPage/', views.calenderPage, name='calenderPage'),
    path('workoutRoutinePage/', views.workoutRoutinePage, name='workoutRoutinePage'), 
    path('prsPage/', views.prsPage, name='prsPage'),
    path('exploreWorkoutsPage/', views.exploreWorkoutsPage, name='exploreWorkoutsPage')
]