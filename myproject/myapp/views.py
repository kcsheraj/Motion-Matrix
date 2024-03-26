from django.shortcuts import render, redirect
from .models import PRModel  # Import your model
from .models import WorkoutRoutine  # Import your WorkoutRoutine model
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.contrib import messages
from django.utils import timezone
from datetime import datetime
import re
import json
from django.core.serializers import serialize
from django.http import JsonResponse
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

def dashboardPage(request):
    # Add your view logic here
    return render(request, 'dashboardPage.html')
    
def calendarPage(request):
    # Add your view logic here
    return render(request, 'calendarPage.html')
    
def workoutRoutinePage(request):
    # Retrieve workout data for the current user
    user = request.user
    workout_routine = WorkoutRoutine.objects.filter(user=user).first()  # Assuming there's only one routine per user

    # Construct JSON object manually
    serialized_workout_routine = {
        'monday': workout_routine.monday,
        'tuesday': workout_routine.tuesday,
        'wednesday': workout_routine.wednesday,
        'thursday': workout_routine.thursday,
        'friday': workout_routine.friday,
        'saturday': workout_routine.saturday,
        'sunday': workout_routine.sunday,
    }

    # Convert the dictionary to JSON format
    serialized_workout_routine_json = json.dumps(serialized_workout_routine)

    # Pass workout data to the template context as JSON
    return render(request, 'workoutRoutinePage.html', {'workout_routine': serialized_workout_routine_json})

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

from django.http import JsonResponse
from .models import WorkoutRoutine

def save_workout(request):
    if request.method == "POST":
        day = request.POST.get("day")
        workout_text = request.POST.get("workoutText")
        user = request.user

        # Check if a WorkoutRoutine instance already exists for the user
        workout_routine = WorkoutRoutine.objects.filter(user=user).first()

        if workout_routine:
            # If a WorkoutRoutine instance exists, update it
            setattr(workout_routine, day, workout_text)
            workout_routine.save()
        else:
            # If no WorkoutRoutine instance exists, create a new one
            workout_routine = WorkoutRoutine.objects.create(user=user)
            setattr(workout_routine, day, workout_text)
            workout_routine.save()

        return JsonResponse({"success": True})
    else:
        return JsonResponse({"success": False})