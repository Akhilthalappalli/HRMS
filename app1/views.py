from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from app1.forms import EmployeeForm,RoleForm,AttendanceForm, SalaryForm
from app1.models import add_holiday
from app1.forms import HolidayForm
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from app1.forms import UserForm, RolePermissionForm
from app1.models import User, UserRole, RolePermission, MenuMaster, Salary, Employee
from.import models
import datetime


# Create your views here.
def dashboard(request):
    emp = Employee.objects.all()
    return render(request,'dashboard.html',{"data":emp})

def sidebar(request):
    return render(request,'sidebar.html')


# def employee(request):
#     return render(request,'employee_reg.html')

def saveEmployee(request):
    #if not request.session.has_key('username'):
        #return HttpResponseRedirect('login')
    print("new")
    form = EmployeeForm()
    if request.method == 'POST':
        print("called")
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('dashboard')
        # else:
        #     return HttpResponseRedirect('dashboard')

    return render(request,'employee_reg.html',{"form":form})

def employee_view(request):

    emp = Employee.objects.all()
    return render(request,'employee_view.html',{"data":emp})


def holiday(request):
    #if not request.session.has_key('username'):
        #return HttpResponseRedirect('login')

    newform = HolidayForm()
    if request.method == 'POST':

        newform = HolidayForm(request.POST)
        if newform.is_valid():
            newform.save()

            return HttpResponseRedirect('holiday')
        else:
            return HttpResponseRedirect('dashboard')

    return render(request,'addholiday.html',{"newform":newform})





def employee_grid_view(request):
    # return render(request,'employee_grid_view.html')
    emp = Employee.objects.all()
    return render(request,'employee_grid_view.html',{"data":emp})

def search(request):
    query=request.POST.get("q" or None)
    emp = Employee.objects.all()

    if query is not None:
            emp = emp.filter(
            Q(empid__icontains=query) |
            Q(fname__icontains=query)
            )

    return render(request,'employee_view.html',{"data":emp})

def grid_search(request):
    query=request.POST.get("q" or None)
    emp = Employee.objects.all()

    if query is not None:
            emp = emp.filter(
            Q(empid__icontains=query) |
            Q(fname__icontains=query)
            )

    return render(request,'employee_grid_view.html',{"data":emp})


# def holiday_view(request):
#     frm = add_holiday.objects.all()
#     return render(request,'holiday_view.html',{"data":frm})

def holiday_view(request):

    frm = add_holiday.objects.all()
    return render(request,'holiday_view.html',{"data":frm})


def holiday_search(request):
    query=request.POST.get("q" or None)
    hly = add_holiday.objects.all()

    if query is not None:
            hly = hly.filter(
            Q(holiday_date__icontains=query))

    return render(request,'holiday_view.html',{"data":hly})


def usertable(request):
    usr = User.objects.all()
    return render(request, 'usertable.html',{"data": usr})


def roletable(request):
    data = UserRole.objects.all()
    return render(request, 'roletable.html',{"data":data})


def roleadd(request):
    form = RoleForm()
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('roletable')
        else:
            return HttpResponse("*****ERROR IN VALIDATION******")
    return render(request, 'roleadd.html',{"form":form})

def rolepermission(request):
    role_id = int(request.GET.get("id",-1))
    data=''
    form = RolePermissionForm()

    if role_id > 0:
        data = RolePermission.objects.all().filter(role = role_id)

        if request.method == 'POST':
            #print("&&&&&&&&&&&&&&")
            #print(str(request.POST))

            #Delete existing
            for item in data:
                item.delete()

            for m in MenuMaster.objects.all():
                opt = request.POST.getlist(str(m))

                if len(opt) > 0:
                    obj = RolePermission.objects.create(
                        role=UserRole.objects.get(id=role_id),
                        menu=m,
                        show='Show' in opt,
                        create='Create' in opt,
                        edit='Edit' in opt,
                        delet='Delete' in opt)
            return redirect('roletable')
        #else:
            #return HttpResponse("*****ERROR IN VALIDATION******")
    return render(request, 'RolePermission.html',{"form":form, "data":data})


def saveUser(request):
    # if not request.session.has_key('username'):
    # return HttpResponseRedirect('login')
    print("new")
    form = UserForm()
    if request.method == 'POST':
        print("called")
        form = UserForm(request.POST, request.FILES)
        print("ok")
        if form.is_valid():
            form.save()
            return redirect('usertable')
        else:
            return HttpResponse("*****ERROR IN VALIDATION******")
    return render(request, 'useradd.html', {"form": form})

def manage(request):
    usr_id = int(request.GET["id"])
    form = UserForm()
    if usr_id > 0 :
        ob = User.objects.get(id=usr_id)
        form = UserForm(instance= ob)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if usr_id > 0:
            form = UserForm(request.POST, request.FILES, instance=ob)
        if form.is_valid():
            form.save()
            return redirect('usertable')

    return render(request, 'useradd.html', {"form": form, "id": usr_id})

def delete(request, usr_id):
    ob = User.objects.get(id=usr_id)
    if ob:
        ob.delete()
        return redirect('usertable')

    return HttpResponse('Error: Invalid Record')

def searchUser(request):
    query = request.POST.get("q")
    usr = User.objects.all()
    if query is not None:
        usr = usr.filter(
            Q(username__icontains=query) |
            Q(fullname__icontains=query)

        )
    return render(request, 'usertable.html', {"data": usr})


def manage_employee(request):


    manage_employee_id = int(request.GET["id"])

    empimage=''

    form = EmployeeForm()
    if manage_employee_id > 0:
        employee_record = Employee.objects.get(id = manage_employee_id)
        form = EmployeeForm(instance=employee_record)
        empimage = employee_record.picture


    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if manage_employee_id > 0:
            form = EmployeeForm(request.POST, request.FILES,instance= employee_record)

        if form.is_valid():
             form.save()
             return HttpResponseRedirect('/employee_view')

    return render(request,'employee_reg.html',{"form":form,"id":manage_employee_id,"empimage":empimage})

def employee_delete(request, employee_id):
    employee_record = Employee.objects.get(id = employee_id)

    if employee_record:
        employee_record.delete()
        return HttpResponseRedirect('/employee_view')

    return HttpResponse("Error: Invalid Record")

def holiday_delete(request, holiday_id):
    holiday_record = add_holiday.objects.get(id = holiday_id)

    if holiday_record:
        holiday_record.delete()
        return HttpResponseRedirect('/holiday_view')

    return HttpResponse("Error: Invalid Record")

def manage_holiday(request):


    manage_holiday_id = int(request.GET["id"])



    newform = HolidayForm()
    if manage_holiday_id > 0:
        holiday_record = add_holiday.objects.get(id = manage_holiday_id)
        newform = HolidayForm(instance=holiday_record)


    if request.method == 'POST':
        newform = HolidayForm(request.POST)
        if manage_holiday_id > 0:
            newform = HolidayForm(request.POST,instance= holiday_record)

        if newform.is_valid():
             newform.save()
             return HttpResponseRedirect('/holiday_view')

    return render(request,'addholiday.html',{"newform":newform,"id":manage_holiday_id})



def attendance_view(request):
    # data = attendance.objects.all()
    # print("*************************************************************")
    # print(data),{"data":data}
    data=models.attendance.objects.all()
    return render(request,"attendance_view.html",{'data':data})

def attendance_search(request):
    query=request.POST.get("q" or None)
    att = models.attendance.objects.all()


    if query is not None:
            att = att.filter(
            Q(attendance_date__icontains=query)
            )

    return render(request,'attendance_view.html',{"data":att})
def attendance_header(request):
    emp = Employee.objects.all()
    tdy = datetime.date.today()

    form = AttendanceForm()
    if request.method == 'POST':

        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()

            # messages.success(request, 'Form submission successful')

            return HttpResponseRedirect('attendance_header')
        else:
            return HttpResponseRedirect('dashboard')

    return render(request,'attendance_header.html',{"form":form,"data":emp,"data1":tdy})

def manage_attendance(request):
    manage_attendance_id = int(request.GET["id"])
    form = AttendanceForm()
    if manage_attendance_id > 0:
        # attendance_record = attendance.objects.get(id = manage_attendance_id)
        attendance_record=models.attendance.objects.get(id=manage_attendance_id)
        form = AttendanceForm(instance=attendance_record)
    if request.method == 'POST':
        form = AttendanceForm(request.POST, request.FILES)
        if manage_attendance_id > 0:
            form = AttendanceForm(request.POST,instance= attendance_record)

        if form.is_valid():
             form.save()
             return HttpResponseRedirect('/attendance_view')
    return render(request,'attendance_header.html',{'form':form,'id':manage_attendance_id})
def attendance_delete(request,attendance_id):
    attendance_delete_record=models.attendance.objects.get(id=attendance_id)
    if attendance_delete_record:
        attendance_delete_record.delete()
        return HttpResponseRedirect('/attendance_view')

def salaryren(request):
    sal1= Salary.objects.all()
    # form = salaryForm()
    # if request.method == 'POST':
    #     print("qqqqqqqqqqq")
    #     form = salaryForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         print("wwwwwwwwwwwwww")
    #         form.save()
    #         return HttpResponseRedirect('salary')
    #     else:
    #         print("############INVALID FORM############")
    return render(request,'Salary.html',{"sal1":sal1},) #,"hra_rate":0.3,"ma_rate":-0.1,"da_rate":0.2,"ta_rate":0.1,"pf_rate":-0.25,"tax_rate":-0.2,"e-total_rate":("da_rate"+"hra_rate"+"ta_rate")})

def addsalary(request):
    form = SalaryForm()
    if request.method == 'POST':
        print("qqqqqqqqqqq")
        form = SalaryForm(request.POST, request.FILES)
        if form.is_valid():
            print("wwwwwwwwwwwwww")
            form.save()
            return HttpResponseRedirect('salaryren')
        else:
            print("############INVALID FORM############")
    return render(request,'addsalary.html',{"form":form},) #,"hra_rate":0.3,"ma_rate":-0.1,"da_rate":0.2,"ta_rate":0.1,"pf_rate":-0.25,"tax_rate":-0.2,"e-total_rate":("da_rate"+"hra_rate"+"ta_rate")})


def editsalary(request, salid):
    ob = Salary.objects.get(id=salid)
    form = SalaryForm(instance = ob)
    if request.method == 'POST':
        print("qqqqqqqqqqq")
        form = SalaryForm(request.POST, request.FILES, instance=ob)
        if form.is_valid():
            print("wwwwwwwwwwwwww")
            form.save()
            return HttpResponseRedirect('salaryren')
        else:
            print("############INVALID FORM############")
    return render(request,'addsalary.html',{"form":form},) #,"hra_rate":0.3,"ma_rate":-0.1,"da_rate":0.2,"ta_rate":0.1,"pf_rate":-0.25,"tax_rate":-0.2,"e-total_rate":("da_rate"+"hra_rate"+"ta_rate")})

def deletesalary(request, salid):
    ob = Salary.objects.get(id=salid)
    if ob:
        ob.delete()
        return redirect('salaryren')
