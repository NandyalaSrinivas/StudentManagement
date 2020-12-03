from django.shortcuts import render, redirect, get_object_or_404
from appstudent.models import Register, Application
from appstudent.forms import RegisterForm, ApplicationForm
from django.http import HttpResponse
from django.urls import reverse


def home(request):
    return render(request, "appstudent/home.html")


def application(request):
    if request.method == 'POST':
        applyform = ApplicationForm(request.POST)
        if applyform.is_valid():
            applyform.save()
            return redirect('/home')
    else:
        applyform = ApplicationForm()
        return render(request, "appstudent/applysform.html", {"applyform": applyform})


def registration(request):
    if request.method == 'POST':
        regform = RegisterForm(request.POST, request.FILES)
        if regform.is_valid():
            regform.save()
            return redirect('/home')
    else:
        regform = RegisterForm()
        return render(request, "appstudent/registerform.html", {"regform": regform})


def candidatelist(request):
    data = Register.objects.values("fastname", "email", "department", "mobile")
    #data = Application.objects.raw('select fullname, email, department,  from appstudent_application where is_verified = True')
    return render(request, "appstudent/candidatelist.html", {'data': data})


def status(request):
    data = Application.objects.raw('select id,email from appstudent_application where is_verified = True')
    email_list = [ele for ele in data]
    if input("enter email") in email_list:
        return redirect("registration")
    #return HttpResponse("You are not eligible")
    return redirect('home')


def student_info(request, application_id):
    data = get_object_or_404(Register, pk=application_id)
    return render(request, "appstudent/studentinfo.html", {'data': data})


def departments(request):
    data = Register.objects.values('department').distinct()
    return render(request, "appstudent/Departments.html", {"data": data})


def department_wise(request, department):
    data = Register.objects.filter(department__contains=department).values()
    return render(request, "appstudent/DepartmentList.html", {"data": data})


