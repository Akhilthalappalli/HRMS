from django.contrib import admin
from app1.models import Gender,MaritalStatus,Designation,Department,Employee,add_holiday,Salary
from app1.models import UserRole,UserStatus,User,MenuMaster,RolePermission,attendance,Leave,Leave_status

# Register your models here.

admin.site.register(Gender)
admin.site.register(MaritalStatus)
admin.site.register(Designation)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(add_holiday)
admin.site.register(UserRole)
admin.site.register(UserStatus)
admin.site.register(User)
admin.site.register(MenuMaster)
admin.site.register(RolePermission)
admin.site.register(attendance)
admin.site.register(Salary)
admin.site.register(Leave)
admin.site.register(Leave_status)
