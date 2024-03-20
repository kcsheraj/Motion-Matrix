from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class PRModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bench_pr = models.TextField(blank=True)
    squat_pr = models.TextField(blank=True)
    deadlift_pr = models.TextField(blank=True)