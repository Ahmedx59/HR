from django import forms
from .models import Employee , Position

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude ='__all__'

class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        exclude ='__all__'