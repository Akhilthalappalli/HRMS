from django import forms
from app1.models import Employee
from app1.models import add_holiday

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

    #def clean_regno(self):
        #rno = self.cleaned_data['regno']
        #if (not rno.isdigit()) or (len(rno) != 4):
            #raise forms.ValidationError('Code Must be Numeric with 4 digits')
        #return rno
class HolidayForm(forms.ModelForm):
    class Meta:
        model = add_holiday
        fields = '__all__'
