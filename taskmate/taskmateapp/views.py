from django.shortcuts import render, HttpResponse

from .models import Employee, Department
from .models import Department, Role

# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    print(context)
    return render(request, 'all_emp.html',context)

def add_emp(request):
   

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dept_id = request.POST.get('dept')  
        salary = int(request.POST.get('salary', 0))
        bonus = int(request.POST.get('bonus', 0))
        role_id = int(request.POST.get('role', 0))
        phone = int(request.POST.get('phone', 0))
        hire_date = request.POST.get('hire_date')

        
        department = Department.objects.get(id=dept_id)
        role = Role.objects.get(id=role_id)

        newemp = Employee(
            first_name=first_name,
            last_name=last_name,
            salary=salary,
            bonus=bonus,
            phone=phone,
            hire_date=hire_date,
            dept_id=department,  
            role_id=role
        )

        newemp.save()
        return HttpResponse('Employee added successfully!')
    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse('An exception occurred! Employee is not added.')
    
    


def remove_emp(request):
    return render(request, 'remove_emp.html')

def filter_emp(request):
    return render(request, 'filter_emp.html')
