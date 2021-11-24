from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from SocaProject import settings
from django.core.mail import *
from django.template.loader import render_to_string
from . tokens import generate_token
from django.utils.encoding import force_bytes,force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site


# Create your views here.
def home(request):return render(request,"authentication/index.html")

def signup(request):
   if request.method == "POST":
         username=request.POST["username"]
         fname=request.POST["fname"]
         lname=request.POST["lname"]
         email=request.POST["email"]
         pass1=request.POST["pass1"]
         pass2=request.POST["pass2"]
         date=request.POST["date"]
         team=request.POST["pickteam"]

         if User.objects.filter(username=username):
           messages.error(request, "Username already exist!Please pick another username.")
           return redirect('signup')

         if User.objects.filter(email=email):
           messages.error(request, "Email already registered under an account!")
           return redirect('signup')

         if len(username)>20:
           messages.error(request, "Username must be under 20 characters")
           return redirect('signup')

         if pass1!=pass2:
            messages.error(request,"Passwords do not match")
            return redirect('signup')

         if not username.isalnum():
            messages.error(request,"Username must be alpha-numeric!")
            return redirect('signup')


         myuser=User.objects.create_user(username,email,pass1)
         myuser.first_name = fname
         myuser.last_name = lname
         myuser.fave_team = team
         myuser.is_active = True
         #myuser.team_name = team
         myuser.save()
         messages.success(request,"Your account has been successfully created!")

         #Welcome Email
         subject = "Welcome to Soca-Scores"
         message = "Hello" + myuser.first_name + "!! \n" + "Welcome to SocaScores!!\nThank you for joining the Soca-Scores\n.This email serves as your confirmation email. Enjoy your time with us. \n\nChairman\nNyambok Julius"
         from_email = settings.EMAIL_HOST_USER
         to_list = [myuser.email]
         send_mail(subject, message, from_email, to_list, fail_silently=True)


         return redirect('signin')

   return render(request,"authentication/signup.html")

def signin(request):
   if request.method == "POST":
     username = request.POST['username']
     pass1 = request.POST['pass1']
     user = authenticate(username=username, password=pass1)

     if user is not None:
        login(request,user)
        fname=user.first_name
        return render(request,"authentication/index.html", {'fname':fname})

     else:
        messages.error(request, "Invalid Credentials entered!")
        return redirect('home')
   return render(request,"authentication/signin.html")


def signout(request):
   logout(request)
   messages.success(request,"Account was signed out successfully")
   return redirect ('home')