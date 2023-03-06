from django.db import models


# Create your models here.


class Department (models.Model):
    department_id = models.CharField (max_length=10, unique=True)
    department_name = models.CharField (max_length=100, unique=True)

    def __str__(self):
        return self.department_name

    class Meta:
        db_table = "department"


Gender_choice = [('male', 'MALE'),
                 ('female', 'Female'),
                 ]


class Employee (models.Model):
    department = models.ForeignKey (Department, on_delete=models.DO_NOTHING)
    e_id = models.IntegerField (unique=True)
    e_name = models.CharField (max_length=100)
    e_dob = models.DateField ( )
    e_email = models.EmailField (unique=True)
    e_contact = models.IntegerField ( )
    e_gender = models.CharField (max_length=6, choices=Gender_choice, default='female')

    def __str__(self):
        # return self.e_email
        return f"{self.e_email}"

    class Meta:
        db_table = "employee"

    projects = models.ManyToManyField ('Project', through='Assignment', through_fields=('employee', 'project'))


class Project (models.Model):
    department = models.ForeignKey (Department, on_delete=models.DO_NOTHING)
    p_name = models.CharField (max_length=50, unique=True)

    def __str__(self):
        return self.p_name

    class Meta:
        db_table = "project"

    employees = models.ManyToManyField ('Employee', through='Assignment', through_fields=('project', 'employee'))


Relation_choice = [('spouse', 'SPOUSE'), ('child', 'CHILD'), ('Father', 'FATHER'), ('Mother', 'MOTHER')]


class Dependent (models.Model):
    employee = models.ForeignKey (Employee, on_delete=models.CASCADE)
    d_name = models.CharField (max_length=100)
    d_relation = models.CharField (max_length=6, choices=Relation_choice, default='blank')
    d_dob = models.DateField ( )
    e_gender = models.CharField (max_length=6, choices=Gender_choice, default='female')

    def __str__(self):
        d_name = self.d_name
        d_rel = self.d_relation
        return '%s : %s' % (d_name, d_rel)

    class Meta:
        db_table = "dependents"


class Assignment (models.Model):
    employee = models.ForeignKey (Employee, on_delete=models.DO_NOTHING)
    project = models.ForeignKey (Project, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = (('employee', 'project'),)

    def __str__(self):
        e_email = self.employee
        p_name = self.project
        return '%s : %s' % (e_email, p_name)
