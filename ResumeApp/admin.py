from django.contrib import admin
from . models import PersonalInfo, Project, Skill, Education

# Register your models here.
admin.site.register(PersonalInfo)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Education)
