from email import message
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request,"authen/index.html")
   
def register(request):

    if request.method == "POST":

      fname = request.POST['fname']
      lname = request.POST['lname']
      uname = request.POST['uname']
      email = request.POST['email']
      pass1 = request.POST['pass1']
      pass2 = request.POST['pass2']
      

      myuser = User.objects.create_user(uname, email, pass1)
      myuser.first_name=fname
      myuser.last_name=lname

      myuser.save()

      messages.success(request, "Your account has been successfully created")

      return redirect('signin')



    return render(request,"authen/register.html")

#def signin(request):

#    if request.method == "POST":
#        uname = request.POST['uname']
#        pass1 = request.POST['pass1']
#
#        user=authenticate(uname='uname',pass1='pass1')
#
#        if user is not None:
#            login(request, user)
#            fname = user.first_name
#            return render(request, "authen/index.html",{'fname':fname})
#        
#        else:
#            messages.error(request,"Bad Credentials")
#            return redirect('home')    


        
#    return render(request,"authen/signin.html")

