
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
    path('exploreWorkoutsPage/', views.exploreWorkoutsPage, name='exploreWorkoutsPage'),
    path('add_text/', views.add_text, name='add_text'),  # New URL pattern for adding text

    # New URL patterns for adding PRs for each lift type
    path('add_bench_pr/', views.add_bench_pr, name='add_bench_pr'),
    path('add_squat_pr/', views.add_squat_pr, name='add_squat_pr'),
    path('add_deadlift_pr/', views.add_deadlift_pr, name='add_deadlift_pr'),

    path('save_workout/', views.save_workout, name='save_workout'),
]