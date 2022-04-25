from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
# from django.template import loader
from sale_management.models import Employee


# Create your views here.


def test(request):
    return HttpResponse('This is working properly!')


def frontpage(request):
    return render(request, 'front_page.html')


def homepage(request):
    return render(request, 'homepage.html')


def about(request):
    return render(request, 'about.html')


def detail(request, employee_id):
    # try:
    #     employee = Employee.objects.get(pk=employee_id)
    # except Employee.DoesNotExist:
    #     raise Http404("Employee does not exist")
    # return HttpResponse(employee)
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, 'sale_management/employee/detail.html', {'employee': employee})


def listing(request):
    latest_employee_list = Employee.objects.order_by('-created_at')[:5]
    context = {
        'latest_employee_list': latest_employee_list
    }
    # template = loader.get_template('sale_management/employee/index.html')
    # output = ', '.join([e.name for e in latest_employee_list])
    # return HttpResponse(template.render(context, request))
    return render(request, 'sale_management/employee/index.html', context)
