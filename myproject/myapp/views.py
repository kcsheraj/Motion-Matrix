from django.shortcuts import render, redirect
from .models import PRModel  # Import your model
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.contrib import messages
from django.utils import timezone
from datetime import datetime, date
import re
# Create your views here.

# Create your views here.
def landingPage(request):
    return render(request, "landingPage.html")

def loginPage(request):
    # Add your view logic here
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'UserName or password doesnt match')
            return render(request, 'loginPage.html')

        user = authenticate(request, username=username, password = password)

        if user is not None:
            login(request,user)
            return redirect('dashboardPage')
        else:
            messages.error(request, 'UserName or password doesnt match')
        
        
    return render(request, 'loginPage.html')

def signUpPage(request):
    # Add your view logic here
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect('loginPage')
        else:
            messages.error(request, 'An error occurred during registration')
   
    return render(request, 'signUpPage.html', {'form': form})
'''
def dashboardPage(request):
    # Add your view logic here
    return render(request, 'dashboardPage.html') '''

def dashboardPage(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # If authenticated, retrieve the first name
        first_name = request.user.first_name
        # Use the first name if available, otherwise fallback to "user"
        name_to_display = first_name if first_name else "admin"
    else:
        # If not authenticated, fallback to "user"
        name_to_display = "user"

    # Pass the name_to_display to the template context
    context = {'display_name': name_to_display}
    
    # Render the dashboard page with the name_to_display in the context
    return render(request, 'dashboardPage.html', context)
    
def calendarPage(request):
    # Add your view logic here
    return render(request, 'calendarPage.html')
    
def workoutRoutinePage(request):
    # Add your view logic here
    return render(request, 'workoutRoutinePage.html')

def prsPage(request):
    user = request.user
    bench_prs = PRModel.objects.filter(user=user).values_list('bench_pr', flat=True)
    squat_prs = PRModel.objects.filter(user=user).values_list('squat_pr', flat=True)
    deadlift_prs = PRModel.objects.filter(user=user).values_list('deadlift_pr', flat=True)
    return render(request, 'prsPage.html', {'bench_prs': bench_prs, 'squat_prs': squat_prs, 'deadlift_prs': deadlift_prs})

def add_bench_pr(request):
    if request.method == 'POST':
        user = request.user
        bench_pr_text = request.POST.get('bench_pr_text')
        # Check if the input consists of only numbers
        if bench_pr_text.isdigit():
            # If it's a number, append "lbs" at the end
            bench_pr_text += " lbs"
            date_added = timezone.now().strftime("%B %d, %Y")
            PRModel.objects.create(user=user, bench_pr=f"{date_added}: {bench_pr_text}")
            return redirect('prsPage')  # Redirect only after adding Bench PR
        else:
            # If not, return to the PRs page without adding and show a warning message
            return redirect('prsPage')
    return redirect('prsPage')


def add_squat_pr(request):
    if request.method == 'POST':
        user = request.user
        squat_pr_text = request.POST.get('squat_pr_text')
        # Check if the input consists of only numbers
        if squat_pr_text.isdigit():
            # If it's a number, append "lbs" at the end
            squat_pr_text += " lbs"
            date_added = timezone.now().strftime("%B %d, %Y")
            PRModel.objects.create(user=user, squat_pr=f"{date_added}: {squat_pr_text}")
        # Redirect back to the PRs page
    return redirect('prsPage')

def add_deadlift_pr(request):
    if request.method == 'POST':
        user = request.user
        deadlift_pr_text = request.POST.get('deadlift_pr_text')
        # Check if the input consists of only numbers
        if deadlift_pr_text.isdigit():
            # If it's a number, append "lbs" at the end
            deadlift_pr_text += " lbs"
            date_added = timezone.now().strftime("%B %d, %Y")
            PRModel.objects.create(user=user, deadlift_pr=f"{date_added}: {deadlift_pr_text}")
        # Redirect back to the PRs page
    return redirect('prsPage')

def add_text(request):
    if request.method == 'POST':
        new_text = request.POST.get('new_text')
        # Save the new text to the database
        PRModel.objects.create(text=new_text)
        # Redirect back to the PRs page after adding the text
        return redirect('prsPage')
    else:
        # Handle other HTTP methods if needed
        return HttpResponse('Method Not Allowed', status=405)

def exploreWorkoutsPage(request):
    # Add your view logic here
    return render(request, 'exploreWorkoutsPage.html')

def date_today(request):
    #fetches current date for the navbar
    current_date = date.today()
    return render(request, 'layout2.html', {'current_date': current_date})