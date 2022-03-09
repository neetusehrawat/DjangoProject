from django import forms
from employee.models import Department, Employee, Dependent, Project, Assignment


class DepartmentForm (forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"


class EmployeeForm (forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["department", "e_id", "e_name", "e_dob", "e_email", "e_contact", "e_gender", ]


class DependentForm (forms.ModelForm):
    class Meta:
        model = Dependent
        fields = "__all__"


class ProjectForm (forms.ModelForm):
    class Meta:
        model = Project
        fields = ["department", "p_name"]


class AssignmentForm (forms.ModelForm):
    class Meta:
        model = Assignment
        fields = "__all__"

# class EmployeeForm (forms.ModelForm):
# department = forms.ModelChoiceField (queryset=Department.objects.all ( ), initial=0)
# e_id = forms.IntegerField ()
# e_name = forms.CharField ()
# e_dob = forms.DateField ( )
# e_email = forms.EmailField ( )
# e_contact = forms.IntegerField ( )
# e_gender = forms.ChoiceField (required=True, choices=Gender_choice)
