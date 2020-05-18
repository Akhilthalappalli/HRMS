from django.contrib import admin
from app1.models import Gender,MaritalStatus,Designation,Department,Employee,add_holiday
from app1.models import UserRole,UserStatus,User

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
