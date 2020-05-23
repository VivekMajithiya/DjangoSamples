from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import UserInfo
from AppTwo import forms

# Create your views here.
def index(request):
    return render(request,'AppTwo/index.html',context=None)

def userinfo(request):
    Users_List = UserInfo.objects.order_by('First_Name')
    userform1 = forms.Usersignup
    user_dict = {'user_temp_ref':Users_List,'userform1':userform1}

    if request.method == 'POST':
        userform1 = forms.Usersignup(request.POST)

        if userform1.is_valid():
            userform1.save()

            return render(request,'AppTwo/userinfo.html',context=user_dict)

        else:
            print('Error saving form data')

    return render(request,'AppTwo/userinfo.html',context=user_dict)

def formpage(request):
    form = forms.Formpage()

    if request.method == 'POST':
        form = forms.Formpage(request.POST)

        if form.is_valid():
            print ('Name :' + form.cleaned_data['name'])
            print ('Name :' + form.cleaned_data['email'])
            print ('Name :' + form.cleaned_data['text'])

    return render(request,'AppTwo/formpage.html',{'form':form})

def usersignup(request):
    userform = forms.Usersignup

    if request.method == 'POST':
        userform = forms.Usersignup(request.POST)

        if userform.is_valid():
            userform.save()

            return userinfo(request)

        else:
            print('Error saving form data')

    return render(request,'AppTwo/usersignup.html',{'userform':userform})
