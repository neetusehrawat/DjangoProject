"""Neetu630FinalProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from employee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home),
    path('departments/',views.view_departments),
    path('add_department/',views.view_add_department),
    path('edit_department/<int:id>',views.view_edit_Department),
    path('departments/<int:id>',views.view_deptemployees),
    path ('projects/<int:id>', views.view_dept_projects),
    path('employees/',views.view_employee),
    path('add/',views.view_add_employee),
    path('employees/<int:id>',views.view_edit_employee),
    path('dependents/<int:id>',views.view_dependents),
    path('delete/<int:id>',views.view_delete_employee),
    path('edit_dependent/<int:id>',views.view_edit_dependent),
    path('delete_dependent/<int:id>',views.view_delete_dependent),
    path ('projects/', views.view_projects),
    path ('add_project/', views.view_add_project),
    path ('edit_project/<int:id>', views.view_edit_project),
    path ('delete_projects/<int:id>', views.view_delete_project),
    path ('view_emp_projects/<int:id>', views.view_emp_assignment),
    path ('view_projects_employees/<int:id>', views.view_project_employees),
    path ('assignments/', views.view_assignment),
    path ('add_assignment/', views.view_add_assignment),
]
