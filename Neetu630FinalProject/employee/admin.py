from django.contrib import admin

# Register your models here.
from employee.models import Employee, Department, Project, Dependent, Assignment


# admin.site.register (Department)
# admin.site.register (Employee)
# admin.site.register (Project)
# admin.site.register (Dependent)
# admin.site.register (Assignment)


@admin.register (Employee)
class EmployeeAdmin (admin.ModelAdmin):
    list_display = ("department","e_id", "e_name", "e_dob", "e_email", "e_contact", "e_gender")


@admin.register (Department)
class DepartmentAdmin (admin.ModelAdmin):
    list_display = ("department_code", "department_name")


@admin.register (Project)
class ProjectAdmin (admin.ModelAdmin):
    list_display = ("department", "p_name")


@admin.register (Dependent)
class DependentAdmin (admin.ModelAdmin):
    list_display = ("employee","d_name", "d_relation","d_dob","e_gender")


@admin.register (Assignment)
class AssignmentAdmin (admin.ModelAdmin):
    list_display = ("employee","project")
