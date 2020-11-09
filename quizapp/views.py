from .forms import quizMasterForm,participantForm
from django.shortcuts import render
from django.contrib.auth.models import User

def participantRegistration(request):
    registered= False

    if request.method=='POST':
        participantForm=participantForm(data=request.POST)
        if participantForm.is_valid():
            user=set_password(user.password)
            user.save()
            reqistered=True
        else:
            print(participantForm.errors)
    else:
        participantForm=participantForm()

    return render (request,'participantRegistration.html',{'participantForm':participantForm,'registered':reqistered})

def masterRegistration(request):
    if request.method=='POST':
        quizMasterForm=quizMasterForm(data=request.POST)
        if quizMasterForm.is_valid():
            user=set_password(user.password)
            user.save()
            reqistered=True
        else:
            print(quizMasterForm.errors)
    else:
        quizMasterForm=quizMasterForm()
    return render (request,'masterRegistration.html',{'quizMasterForm':quizMasterForm,'registered':reqistered})

def role(request):
    return render(request,'role.html')
