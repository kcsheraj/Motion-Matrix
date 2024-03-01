from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Create your views here.
def landingPage(request):
    return render(request, "landingPage.html")

def loginPage(request):
    # Add your view logic here
    return render(request, 'loginPage.html')

def dashboardPage(request):
    # Add your view logic here
    return render(request, 'dashboardPage.html')
    
def calenderPage(request):
    # Add your view logic here
    return render(request, 'calenderPage.html')
    
def workoutRoutinePage(request):
    # Add your view logic here
    return render(request, 'workoutRoutinePage.html')

def prsPage(request):
    # Add your view logic here
    return render(request, 'prsPage.html')

def exploreWorkoutsPage(request):
    # Add your view logic here
    return render(request, 'exploreWorkoutsPage.html')