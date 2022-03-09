from django.http import HttpResponse

from django.shortcuts import render, redirect

# Create your views here.


from employee.forms import EmployeeForm, DepartmentForm, DependentForm, ProjectForm, AssignmentForm
from employee.models import Department, Employee, Dependent, Project, Assignment


def home(request):
    return render (request, "home.html")


def view_departments(request):
    dept = Department.objects.all ( )
    return render (request, "departments_list.html", {'dept': dept})


def view_add_department(request):
    if request.method == "POST":
        form = DepartmentForm (request.POST)
        if form.is_valid ( ):
            try:
                form.save ( )
                return redirect ('/departments')
            except:
                pass
    else:
        form = DepartmentForm ( )
    return render (request, 'add_department.html', {'form': form})


def view_edit_Department(request, id):
    dept = Department.objects.get (id=id)
    if request.method == "POST":
        form = DepartmentForm (request.POST, instance=dept)
        if form.is_valid ( ):
            try:
                form.save ( )
                return redirect ('/departments')
            except:
                pass
    else:
        form = DepartmentForm (instance=dept)
    return render (request, 'department_edit.html', {'form': form})


def view_deptemployees(request, id):
    dept = Department.objects.get (id=id)
    emp = dept.employee_set.all ( )
    return render (request, "Deptemployee_list.html", {'dept': dept, 'emp': emp})


def view_dept_projects(request, id):
    dept = Department.objects.get (id=id)
    project = dept.project_set.all ( )
    if project.count ( ) == 0:
        # return HttpResponse ("No data")
        return render (request, "no_data.html", {'dept': dept, 'dept': dept})
    else:
        return render (request, "dept_projects.html", {'project': project, 'dept': dept})


def view_employee(request):
    emp = Employee.objects.all ( )
    return render (request, "employee_list.html", {'emp': emp})


def view_add_employee(request):
    if request.method == "POST":
        form = EmployeeForm (request.POST)
        if form.is_valid ( ):
            try:
                form.save ( )
                return redirect ('/employees')
            except:
                pass
    else:
        form = EmployeeForm ( )
    return render (request, 'add_employee.html', {'form': form})


def view_edit_employee(request, id):
    emp = Employee.objects.get (id=id)
    if request.method == "POST":
        form = EmployeeForm (request.POST, instance=emp)
        if form.is_valid ( ):
            try:
                form.save ( )
                return redirect ('/employees')
            except:
                pass
    else:
        form = EmployeeForm (instance=emp)
    return render (request, 'employee_edit.html', {'form': form})


def view_dependents(request, id):
    emp = Employee.objects.get (id=id)
    depend = emp.dependent_set.all ( )
    if depend.count ( ) == 0:
        return render (request, "no_data.html", {'emp': emp, 'depend': depend})
    else:
        return render (request, "dependent_list.html", {'emp': emp, 'depend': depend})


def view_emp_assignment(request, id):
    emp = Employee.objects.get (id=id)
    prj = emp.project_set.all ( )
    if prj.count ( ) == 0:
        return render (request, "no_data.html", {'emp': emp, 'prj': prj})
    else:
        return render (request, "emp_assignment_list.html", {'emp': emp, 'prj': prj})


# def view_delete_employee(request, id):
#     emp = Employee.objects.get (id=id)
#     if request.method == 'POST':
#         emp.delete ( )
#         return redirect ("/employees")
#     return render (request, 'delete_employee.html', {'emp': emp})

def view_delete_employee(request, id):
    emp = Employee.objects.get (id=id)
    prj = emp.project_set.all ( )
    if prj.count ( ) == 0:
        if request.method == 'POST':
            emp.delete ( )
            return redirect ("/employees")
        else:
            return render (request, 'delete_employee.html', {'emp': emp})
    else:
        # return HttpResponse ("Cannot delete employee")
        return render (request, 'employee_no_delete.html', {'emp': emp, 'prj': prj})


def view_edit_dependent(request, id):
    depend = Dependent.objects.get (id=id)
    if request.method == "POST":
        form = DependentForm (request.POST, instance=depend)
        if form.is_valid ( ):
            try:
                form.save ( )
                return redirect ('/employees')
            except:
                pass
    else:
        form = DependentForm (instance=depend)
    return render (request, 'dependent_edit.html', {'form': form})


def view_delete_dependent(request, id):
    depend = Dependent.objects.get (id=id)
    if request.method == 'POST':
        depend.delete ( )
        return redirect ("/employees")
    return render (request, 'delete_dependent.html', {'depend': depend})


def view_projects(request):
    prj = Project.objects.all ( )
    return render (request, "project_list.html", {'prj': prj})


def view_add_project(request):
    if request.method == "POST":
        form = ProjectForm (request.POST)
        if form.is_valid ( ):
            try:
                form.save ( )
                return redirect ('/projects')
            except:
                pass
    else:
        form = ProjectForm ( )
    return render (request, 'add_project.html', {'form': form})


def view_edit_project(request, id):
    prj = Project.objects.get (id=id)
    if request.method == "POST":
        form = ProjectForm (request.POST, instance=prj)
        if form.is_valid ( ):
            try:
                form.save ( )
                return redirect ('/projects')
            except:
                pass
    else:
        form = ProjectForm (instance=prj)
    return render (request, 'project_edit.html', {'form': form})


def view_project_employees(request, id):
    prj = Project.objects.get (id=id)
    emp = prj.employee_set.all ( )
    if emp.count ( ) == 0:
        return render (request, "no_data.html", {'emp': emp, 'prj': prj})
    else:
        return render (request, "project_employees.html", {'emp': emp, 'prj': prj})


# def view_delete_project(request, id):
#     prj = Project.objects.get (id=id)
#     if request.method == 'POST':
#         prj.delete ( )
#         return redirect ("/projects")
#     return render (request, 'delete_project.html', {'prj': prj})

def view_delete_project(request, id):
    prj = Project.objects.get (id=id)
    emp = prj.employee_set.all ( )
    if emp.count ( ) == 0:
        if request.method == 'POST':
            prj.delete ( )
            return redirect ("/projects")
        else:
            return render (request, 'delete_project.html', {'prj': prj})
    else:
        # return HttpResponse ("Cannot delete employee")
        return render (request, 'project_no_delete.html', {'emp': emp, 'prj': prj})


def view_assignment(request):
    assign = Assignment.objects.all ( )
    return render (request, "assignment_list.html", {'assign': assign})


def view_add_assignment(request):
    if request.method == "POST":
        form = AssignmentForm (request.POST)
        if form.is_valid ( ):
            try:
                form.save ( )
                return redirect ('/assignments')
            except:
                pass
    else:
        form = AssignmentForm ( )
    return render (request, 'add_assignment.html', {'form': form})
