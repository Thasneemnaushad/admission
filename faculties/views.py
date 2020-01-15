from django.shortcuts import render
from . import views
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.contrib.auth import logout
from faculties.models import assessment
from students import urls


# Create your views here.
#login 
def signin(request):
    if request.method=='POST':
        username=request.POST.get('email')
        password = request.POST.get('password')
        username=str(username)
        password=str(password)
        if(username=='admin' and password=='admin'):
            return render(request,'faculty-login.html')
        else:
            (username=='student' and password=='student')
            return render(request,'home.html')

  #create assessment in faculty page      
def fassessment(request):
    if request.method=='POST':
        assessment_name=request.POST.get('fa_name')
        date=request.POST.get('fa_date')
        subject=request.POST.get('fa_subject')
        faculty=request.POST.get('fa_faculty')

        a=assessment(assessment_name = assessment_name , date = date , subject = subject , faculty = faculty)
        a.save()
    return render(request,'assessment.html')


#create student details in faculty assessment page
    