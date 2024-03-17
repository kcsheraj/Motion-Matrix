# Generated by Django 4.1.7 on 2024-03-17 18:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("myapp", "0002_prmodel_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="prmodel",
            name="text",
        ),
        migrations.AddField(
            model_name="prmodel",
            name="bench_pr",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="prmodel",
            name="deadlift_pr",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="prmodel",
            name="squat_pr",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="prmodel",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]