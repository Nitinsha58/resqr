# Generated by Django 4.1.1 on 2022-09-24 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResumeApp', '0002_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='desc',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]