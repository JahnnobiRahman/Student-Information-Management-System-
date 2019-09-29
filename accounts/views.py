from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def register(request):

    if request.method=='POST':

        if request.POST['pword']==request.POST['pword2']:
            try:
                user= User.objects.get(username = request.POST['username'])
                return render (request,'accounts/register.html',{'error':'Username has already been taken'})
            except User.DoesNotExist:
                user= User.objects.create_user(request.POST['username'],password=request.POST['pword'])
                auth.login(request,user)
                return redirect ('home')

        else:
            return render (request,'accounts/register.html',{'error':'Passwords must match'})
    else:

        return render (request,'accounts/register.html')


def login(request):
    if request.method=='POST':
        user = auth.authenticate(username=request.POST['username'], password= request.POST['pword'])
        if user is not None:
            auth.login(request,user)
            return redirect ('home')
        else:
            return render (request,'accounts/login.html', {'error': 'username or password is incorrect'})

    else:
        return render (request,'accounts/login.html')



def logout(request):
    #re route to home
    return render(request, 'accounts/login.html')
