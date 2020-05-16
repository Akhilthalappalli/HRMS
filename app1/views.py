from django.shortcuts import render
from django.http import HttpResponseRedirect
from app1.forms import EmployeeForm
from app1.models import Employee
from app1.models import add_holiday
from app1.forms import HolidayForm
from django.db.models import Q

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
