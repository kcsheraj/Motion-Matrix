from django.contrib import admin
from .models import PRModel, WorkoutRoutine

# Register PRModel model here.
admin.site.register(PRModel)

# Register your models here.
admin.site.register(WorkoutRoutine)