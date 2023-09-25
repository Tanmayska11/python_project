
from django.urls import path
from . import views
urlpatterns = [
    path('list/', views.employee_form,name="employee_insert"), # get and post req. for insert   localhost:/employee/list
    path('<uuid:id>/', views.employee_form,name="employee_update"),#get and post req. for update
    path('delete/<uuid:id>/',views.employee_delete,name='employee_delete'),
    path('',views.employee_list,name="employee_list"),# get  req. for retrive and display all records
    path('login/', views.login_page ,name="login_page"),
    path('register/', views.register_page ,name="register_page"),
    path('logout/',views.logout_page,name='logout_page'),
]