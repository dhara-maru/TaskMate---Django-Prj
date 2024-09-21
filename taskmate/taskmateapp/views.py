from django.shortcuts import render

from .models import Employee
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
   

    if request.method == "POST":
        first_name = request.POST.get('first_name')  # Use .get() to avoid KeyError
        last_name = request.POST.get('last_name')
        dept = request.POST.get('dept')
        salary = int(request.POST.get('salary', 0))  # Default to 0 if not found
        bonus = int(request.POST.get('bonus', 0))
        role = request.POST.get('role')
        phone = int(request.POST.get('phone', 0))
        hire_date = request.POST.get('hire_date')

        newemp = Employee(
            first_name=first_name,
            last_name=last_name,
            salary=salary,
            bonus=bonus,
            phone=phone,
            hire_date=hire_date,
            dept=dept,
            role=role
        )
        newemp.save()

    
    
    return render(request, 'add_emp.html')


def remove_emp(request):
    return render(request, 'remove_emp.html')

def filter_emp(request):
    return render(request, 'filter_emp.html')
