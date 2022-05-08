import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import  *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from .helper import ID,password
from django.core.mail import send_mail
from django.contrib import messages



def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=='GET':
        return render(request,'register.html')
    elif request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        mail=request.POST.get('email')
        messages.success(request,'Your Registration is completed. Check Your Email To get User ID and Password')
        

        user_id=ID(fname)
        Password=str(password())

        subject='Welcome To Track_ME!'
        body=f'your user name is {user_id} and your password is {Password}'
        send_mail(
    subject,
    body,
    'utsavpokemon9000chatterjee@gmail.com',
    [mail],
    fail_silently=False,
)


        s=Consumers(first_name=fname,last_name=lname,email=mail)
        s.save()



        user = User.objects.create_user(user_id, mail, Password)
        user.first_name=fname
        user.last_name=lname
        user.save()
              






    return render(request,'register.html')



def loginn(request):
    if request.method=="GET":
        return render(request,'login.html')
    elif request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        if user is not None:

            login(request,user)

            return redirect('home')
        
        
    messages.warning(request,'Wrong Username or Password')   
    return render(request,'login.html')   


def logoutt(request):
    logout(request)
    return redirect('home')

@csrf_exempt
def track(request,st):
    if request.user.is_authenticated:
        if request.method=='GET':
            return render(request,'track.html')
        elif request.method=='POST':
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            lat = (body['lat'])
            long=(body['lon'])
            obj=Pos.objects.filter(userID=st)
            if(obj.exists()):
                c=obj.count()
                if(c==1):
                    x=Pos(idd=c+1,userID=st,latitude=lat,longitude=long)
                    x.save()
                else:
                    x=Pos(idd=1,userID=st,latitude=lat,longitude=long)
                    x.save()
   
            else:
                x=Pos(idd=1,userID=st,latitude=lat,longitude=long)
                x.save()

            
            return render(request,'track.html')
        return render(request,'track.html')



def Map(request,st):
    if request.user.is_authenticated:
        if request.method=='GET':
            return render(request,'map.html')








@api_view(['GET'])
def api(request,st):

    if request.method=='GET':
        request.user.username=st
        r_obj=Pos.objects.filter(userID=request.user.username)

        
        data=[
            
        ]
        if(r_obj.exists()):

            c=r_obj.count()
            print(c)
            for i in range(0,c):
                data.append(([float(r_obj.values('longitude')[i]['longitude']), float(r_obj.values('latitude')[i]['latitude'])]))
         
            return Response(data)
        else:
            return Response({'msg':'no data'})




@api_view(['POST'])
def OthersApi(request,st):
    if request.method=='POST':
        value=(request.data['msg'])
        r_obj=Pos.objects.filter(userID=value)
                
        data=[
            
        ]
        if(r_obj.exists()):

            c=r_obj.count()
            print(c)
            for i in range(0,c):
                data.append(([float(r_obj.values('longitude')[i]['longitude']), float(r_obj.values('latitude')[i]['latitude'])]))
         
            return Response(data)

        return Response({'status':'running'})
