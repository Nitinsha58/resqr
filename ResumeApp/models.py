import uuid
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class PersonalInfo(models.Model):
    TEMPLATE_LIST = (
        (1, "Template 1"),
        (2, "Template 2"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="personal_info")
    template = models.CharField(max_length=65, choices=TEMPLATE_LIST, null=True, default=1, blank=False)
    name = models.CharField(max_length=65, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True )    
    phone = PhoneNumberField(blank=False, null=False)
    city = models.CharField(max_length=65)
    regards = models.CharField(max_length=65, null=True, blank=True)

    def __str__(self):
        return self.name  + "'s profile"

class Project(models.Model):
    user = models.ForeignKey(PersonalInfo, null=True, on_delete=models.CASCADE, related_name="project")
    title = models.CharField(max_length=255, null=True, blank=False )
    link = models.CharField(max_length=255, null=True, blank=True)
    desc = models.TextField(max_length=255, null=True , blank=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    user = models.ForeignKey(PersonalInfo, null=True, on_delete=models.CASCADE, related_name="skill")
    title = models.CharField(max_length=255, null=True, blank=False )

    def __str__(self):
        return self.title

class Education(models.Model):
    user = models.ForeignKey(PersonalInfo, null=True, on_delete=models.CASCADE, related_name="education")
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    title = models.CharField(max_length=255, null=True, blank=False )
    desc = models.TextField(max_length=255, null=True , blank=True)

    def __str__(self):
        return self.title

