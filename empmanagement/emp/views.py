from django.shortcuts import render,redirect
from django.urls import reverse 
from .forms import EmployeeForm
from .models import Employee
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def employee_list(request):
    context = {"employee_list":Employee.objects.all()}
    return render(request,"emp/employee_list.html",context)



@login_required(login_url='/login/')
def employee_form(request,id=''):
    if request.method =='GET':  
        if id=='':      
            form =EmployeeForm()
        else:
            employee =Employee.objects.get(pk=id)
            form =EmployeeForm(instance=employee)
        return render(request,"emp/employee_form.html",{'form':form})
    else:
        if id=='':
            form =EmployeeForm(request.POST)
        else:
            employee =Employee.objects.get(pk=id)
            form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        #return redirect('/employee')
        return redirect(reverse('employee_list'))
    

@login_required(login_url='/login/')
def employee_delete(request,id):
    employee =Employee.objects.get(pk=id)
    employee.delete()
    #return redirect('/employee')
    return redirect(reverse('employee_list'))


def login_page(request):
    if request.method=="POST":    
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid username..')
            return redirect('/login/')
        
        user=authenticate(username=username,password=password)

        if user is None:
            messages.error(request,'Invalid password..')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect(reverse('employee_list'))

    return render(request,'emp/login.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')


def register_page(request):

    if request.method=="POST":
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "User Name is already exist create another..") 
            return redirect('/register/')

        user=User.objects.create(
            email=email,
            username=username,

        )
        user.set_password(password)
        user.save()
        messages.info(request, "Your account created sucessfully..") 
        return redirect('/register/')

    return render(request,'emp/register.html')