from django.shortcuts import render
from django.http import HttpResponseRedirect
from app1.forms import EmployeeForm
from app1.models import Employee
from app1.models import add_holiday
from app1.forms import HolidayForm
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from app1.forms import UserForm
from app1.models import User

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
    return render(request, 'roletable.html')


def roleadd(request):
    return render(request, 'roleadd.html')


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
