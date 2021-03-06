from django.db import models
from datetime import datetime
# Create your models here.

class Gender(models.Model):
    description = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.description

class MaritalStatus(models.Model):
    description = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.description

class Designation(models.Model):
    description = models.CharField(max_length=40,unique=True)

    def __str__(self):
        return self.description

class Department(models.Model):
    description = models.CharField(max_length=40,unique=True)

    def __str__(self):
        return self.description


class Employee(models.Model):
    empid = models.CharField(max_length=10,unique=True)
    fname = models.CharField(max_length=100,  blank=False)
    lname = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    gender = models.ForeignKey(Gender,on_delete=models.CASCADE,)
    picture = models.ImageField(null=True)

    address = models.CharField(max_length=255, blank=True)
    paddress = models.CharField(max_length=255, blank=True)
    dob = models.DateTimeField(null=False)
    mstatus = models.ForeignKey(MaritalStatus,on_delete=models.CASCADE,)
    post = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    designation = models.ForeignKey(Designation,on_delete=models.CASCADE,)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,)
    doj = models.DateTimeField(null=True)
    wemail = models.EmailField(max_length=50)
    wphone = models.CharField(max_length=30)



    def __str__(self):
        return self.fname + ' ' + self.lname


class add_holiday(models.Model):
    holiday_name = models.CharField(max_length=50)
    holiday_date = models.DateTimeField(null=True)
    holiday_description = models.CharField(max_length=100)

class UserRole(models.Model):
    description = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.description


class UserStatus(models.Model):
    description = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.description


class User(models.Model):
    fullname = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=20)
    confirm_password = models.CharField(max_length=20)
    role = models.ForeignKey(UserRole, on_delete=models.CASCADE, )
    status = models.ForeignKey(UserStatus, on_delete=models.CASCADE, )

    def __str__(self):
        return self.username


class MenuMaster(models.Model):
    description = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.description


class RolePermission(models.Model):
    role = models.ForeignKey(UserRole, on_delete=models.CASCADE, )
    menu = models.ForeignKey(MenuMaster, on_delete=models.CASCADE, )
    show = models.BooleanField()
    create = models.BooleanField()
    edit = models.BooleanField()
    delet = models.BooleanField()

class attendance(models.Model):
    attendance_date = models.DateTimeField(blank=True,default=datetime.now())
    attendance_checkin = models.CharField(max_length=100,default="9.00")
    attendance_checkout = models.CharField(max_length=100,default="5.00")
    attendance_emp = models.ForeignKey(Employee,on_delete=models.CASCADE)


class Salary(models.Model):
    designation = models.ForeignKey(Designation,on_delete=models.CASCADE,)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,)
    bp = models.IntegerField()
    da = models.IntegerField()
    ta = models.IntegerField()
    hra = models.IntegerField()
    ma = models.IntegerField()
    pf = models.IntegerField()
    tax = models.IntegerField()
    e_total=models.IntegerField()
    d_total=models.IntegerField()
    total = models.IntegerField()
    totalhand = models.IntegerField()
    # def __str__(self):
    #     return self.designation

class Leave_status(models.Model):
    description = models.CharField(max_length=40,unique=True)

    def __str__(self):
        return self.description

class Leave(models.Model):
    leave_emp = models.ForeignKey(Employee,on_delete=models.CASCADE,)
    leave_type = models.CharField(max_length=100)
    leave_status = models.ForeignKey(Leave_status,on_delete=models.CASCADE,)
    leave_from_date = models.DateTimeField(null=True)
    leave_to_date = models.DateTimeField(null=True)
    leave_msg = models.CharField(max_length=100)
