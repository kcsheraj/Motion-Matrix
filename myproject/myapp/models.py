from django.contrib.auth.models import User
from django.db import models




class PRModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bench_pr = models.TextField(blank=True)
    squat_pr = models.TextField(blank=True)
    deadlift_pr = models.TextField(blank=True)

class WorkoutRoutine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    monday = models.TextField(blank=True)
    tuesday = models.TextField(blank=True)
    wednesday = models.TextField(blank=True)
    thursday = models.TextField(blank=True)
    friday = models.TextField(blank=True)
    saturday = models.TextField(blank=True)
    sunday = models.TextField(blank=True)