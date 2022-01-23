from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import OtherDetails
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from SocaProject import settings
from django.core.mail import *
from django.template.loader import render_to_string
from . tokens import generate_token
from django.utils.encoding import force_bytes,force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from bs4 import BeautifulSoup
from .data_structures import stats
import requests
from django.shortcuts import render
import pandas as pd
import json
import os
import pickle
os.chdir(r"C:\Users\hp\Desktop\Projects\SocaProject")
# Create your views here.

def homepage(request):return render(request,"authentication/homepage.html")


def signup(request):
   if request.method == "POST":
         username=request.POST["username"]
         fname=request.POST["fname"]
         lname=request.POST["lname"]
         email=request.POST["email"]
         pass1=request.POST["pass1"]
         pass2=request.POST["pass2"]
         otherteam=request.POST["noteam"]
         #date=request.POST.get("date_of_birth",False)

         if User.objects.filter(username=username):
           messages.error(request, "Username already exist! Please pick another username.")
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
         myuser.is_active = True
         myuser.save()
         user=User.objects.get(email=email)
         mydetails=OtherDetails(user=user,no_team=otherteam)
         mydetails.save()




         messages.success(request,"Your account has been successfully created!")

         #Welcome Email
         subject = "Welcome to Soca-Scores"
         message = "Hello" +" "+ myuser.username + "!! \n" + "Welcome to SocaScores!!\n Thank you for joining the Soca-Scores.This email serves as your confirmation email. Enjoy your time with us. \n\nChairman\nNyambok Julius"
         from_email = settings.EMAIL_HOST_USER
         to_list = [myuser.email]
         send_mail(subject, message, from_email, to_list, fail_silently=True)


         return redirect('signin')

   return render(request,"authentication/xignup.html")

def signin(request):
   if request.method == "POST":
     username = request.POST['username']
     pass1 = request.POST['pass1']
     user = authenticate(username=username, password=pass1)

     if user is not None:
        login(request,user)
        username=user.username
        request.session['name'] = username
        id=user.id
        other_=OtherDetails.objects.get(user_id=id)
        no_team=other_.no_team
        request.session['team'] = no_team
        return render(request,"authentication/homepage.html", {'username':username,'no_team':no_team})

     else:
        messages.error(request, "Invalid Credentials entered!")
        return redirect('homepage')
   return render(request,"authentication/xignin.html")



def rest_prem(request):
    url = "https://www.skysports.com/premier-league-table"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    team_name = []
    team_played= []
    team_wins = []
    team_draws = []
    team_loss = []
    team_GF = []
    team_GA = []
    team_GD = []
    team_points = []

    team=soup.find('table',{'class':'standing-table__table callfn'}).find('tbody').find_all('tr')
    for r in team:
        team_name.append(r.find('td',class_='standing-table__cell standing-table__cell--name').text.strip())
        team_played.append(r.find_all('td',class_="standing-table__cell")[2].text)
        team_wins.append(r.find_all('td',class_='standing-table__cell')[3].text)
        team_draws.append(r.find_all('td',class_='standing-table__cell')[4].text)
        team_loss.append(r.find_all('td',class_='standing-table__cell')[5].text)
        team_GF.append(r.find_all('td',class_='standing-table__cell')[6].text)
        team_GA.append(r.find_all('td',class_='standing-table__cell')[7].text)
        team_GD.append(r.find_all('td',class_='standing-table__cell')[8].text)
        team_points.append(r.find_all('td',class_='standing-table__cell')[9].text)

    epl_data=pd.DataFrame({'Team':team_name,'MP':team_played,'W':team_wins,'D':team_draws,'L':team_loss,'GF':team_GF,'GA':team_GA,'GD':team_GD,'Pts':team_points})
    team_Data=[]
    allData=[]
    for i in range(epl_data.shape[0]):
            temp=epl_data.iloc[i]
            allData.append(dict(temp))
    no_team=request.session['team']
    username=request.session['name']
    request.session.set_expiry(6000)
    context={'data':allData, 'no_team':no_team,'username':username}
    return render(request,"authentication/table.html",context)


def fixtures(request):
    no_team=request.session['team']
    username=request.session['name']
    request.session.set_expiry(6000)
    context={'no_team':no_team,'username':username}
    return render(request,'authentication/fixtures.html',context)

def squad_stats(request):
    no_team=request.session['team']
    username=request.session['name']
    request.session.set_expiry(6000)
    context={'no_team':no_team,'username':username}
    return render(request,'authentication/squad_stats.html',context)

def my_team_stats(request):
    std_=stats()
    standard_stats=std_.df
    no_team=request.session['team']
    username=request.session['name']
    request.session.set_expiry(6000)
    for index,rows in standard_stats.iterrows():
        if no_team == index:
            i = (rows[0])
    context={'no_team':no_team,'username':username,'i':i}
    return render(request,'authentication/my_std_stats.html',context)

def my_fixtures(request):
    std_=stats()
    standard_stats=std_.df
    no_team=request.session['team']
    username=request.session['name']
    request.session.set_expiry(6000)
    for index,rows in standard_stats.iterrows():
        if no_team == index:
            i = (rows[1])
    context={'no_team':no_team,'username':username,'i':i}
    return render(request,'authentication/my_fixtures.html',context)

def my_shooting(request):
    std_=stats()
    standard_stats=std_.df
    no_team=request.session['team']
    username=request.session['name']
    request.session.set_expiry(6000)
    for index,rows in standard_stats.iterrows():
        if no_team == index:
            i=(rows[2])
    context={'no_team':no_team,'username':username,'i':i}
    return render(request,'authentication/my_shooting.html',context)

def my_minutes(request):
    std_=stats()
    standard_stats=std_.df
    no_team=request.session['team']
    username=request.session['name']
    request.session.set_expiry(6000)
    for index,rows in standard_stats.iterrows():
        if no_team == index:
            i=(rows[3])
    context={'no_team':no_team,'username':username,'i':i}
    return render(request,'authentication/my_minutes.html',context)

def go_to_pred(request):
    no_team=request.session['team']
    username=request.session['name']
    request.session.set_expiry(6000)
    context={'no_team':no_team,'username':username}
    return render(request,'authentication/my_pred.html',context)

def get_pred(request):
    with open("Emp.pickle","rb") as file_handle:
        retrieved_data = pickle.load(file_handle)
        retrieved_data=retrieved_data.replace({0:'Away Win',1:'Draw',2:'Home Win'})
        retrieved_data.columns=['Predictions']
        pred=retrieved_data.sample(ignore_index=True)
        index = pred.index
        team_pred=pred.at[0,'Predictions']
        no_team=request.session['team']
        username=request.session['name']
        request.session.set_expiry(6000)
        context={'no_team':no_team,'username':username,'team':team_pred}
        return render(request,'authentication/my_pred.html',context)


def signout(request):
   logout(request)
   messages.success(request,"Signed out successfully")
   return redirect ('homepage')

