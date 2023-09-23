
from django.urls import path
from . import views
urlpatterns = [
    path('list/', views.employee_form,name="employee_insert"), # get and post req. for insert   localhost:/employee/list
    path('<int:id>/', views.employee_form,name="employee_update"),#get and post req. for update
    path('delete/<int:id>/',views.employee_delete,name='employee_delete'),
    path('',views.employee_list,name="employee_list")# get  req. for retrive and display all records
]