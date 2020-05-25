"""hrm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.home,name="home" ),
    path('',views.dashboard,name="dashboard" ),
    path('dashboard',views.dashboard,name="dashboard" ),
    path('employee',views.saveEmployee,name="employee" ),
    path('employee_view',views.employee_view,name="employee_view" ),
    path('holiday',views.holiday,name="holiday" ),
    path('holiday_view',views.holiday_view,name="holiday_view" ),
    # path('btnemployee',views.btnemployee,name="btnemployee" ),
    path('employee_grid_view',views.employee_grid_view,name="employee_grid_view" ),
     path('search',views.search,name="search" ),
     path('grid_search',views.grid_search,name="grid_search" ),
     path('holiday_search',views.holiday_search,name="holiday_search" ),
    path('useradd',views.saveUser,name='useradd'),
    path('usertable', views.usertable, name='usertable'),
    path('roletable', views.roletable, name='roletable'),
    path('roleadd', views.roleadd, name='roleadd'),
    path('rolepermission', views.rolepermission, name='rolepermission'),
    path('searchUser', views.searchUser, name='searchUser'),
    path('delete/<int:usr_id>', views.delete, name='delete'),
    path('manage', views.manage, name='manage'),
    path('manage_employee', views.manage_employee),
     path('employee_delete/<int:employee_id>',views.employee_delete,name='employee_delete'),
     path('holiday_delete/<int:holiday_id>',views.holiday_delete,name='holiday_delete'),
         path('manage_holiday', views.manage_holiday),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
