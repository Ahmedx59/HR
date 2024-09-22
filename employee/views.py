from django.shortcuts import render
from django.views import generic

from .models import Employee ,Position
from .Forms import EmployeeForm , PositionForm


class EmployeeList(generic.ListView):
    model = Employee



class EmployeeDetail(generic.DeleteView):
    model = Employee



class createEmployee(generic.CreateView):
    model = Employee
    form_class = EmployeeForm



class UpdateEmployee(generic.UpdateView):
    model = Employee
    form_class = EmployeeForm



class DeleteEmployee(generic.DeleteView):
    model = Employee




class LestPosition(generic.ListView):
    model = Position




class DetailPosition(generic.ListView):
    model = Position




class CreatePosition(generic.ListView):
    model = Position
    form_class = PositionForm




class UpdatePosition(generic.ListView):
    model = Position
    form_class = PositionForm





class deletePosition(generic.ListView):
    model = Position