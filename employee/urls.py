from django.urls import path
from .views import EmployeeList , EmployeeDetail , createEmployee ,DeleteEmployee ,UpdateEmployee


app_name = 'employee'

#employee/
urlpatterns = [
    path('',EmployeeList.as_view()),
    path('<int:pk>/',EmployeeDetail.as_view()),
    path('create',EmployeeList.as_view()),
    path('<int:pk>/update',UpdateEmployee.as_view()),
    path('<int:pk>',DeleteEmployee.as_view()),

]