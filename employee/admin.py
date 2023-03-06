from django.contrib import admin

# Register your models here.
from employee.models import Employee, Department, Project, Dependent, Assignment

admin.site.register (Department)
admin.site.register (Employee)
admin.site.register (Project)
admin.site.register (Dependent)
admin.site.register (Assignment)

