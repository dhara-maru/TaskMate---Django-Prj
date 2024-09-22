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
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept_id = request.POST['dept']  # Getting selected department id
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        role_id = request.POST['role']  # Getting selected role id
        phone = request.POST['phone']
        hire_date = request.POST['hire_date']

        dept = Department.objects.get(id=dept_id)  # Get Department instance by id
        role = Role.objects.get(id=role_id)  # Get Role instance by id

        newemp = Employee(first_name=first_name, last_name=last_name, dept_id=dept,
                          salary=salary, bonus=bonus, role_id=role, phone=phone,
                          hire_date=hire_date)
        newemp.save()
        return HttpResponse('Employee added successfully!')
    else:
        departments = Department.objects.all()  # Query all departments
        roles = Role.objects.all()  # Query all roles
        return render(request, 'add_emp.html', {'departments': departments, 'roles': roles})
    
    


def remove_emp(request):
    return render(request, 'remove_emp.html')

def filter_emp(request):
    return render(request, 'filter_emp.html')
