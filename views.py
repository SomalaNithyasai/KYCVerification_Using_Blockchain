from django.shortcuts import render
from django.http import JsonResponse
import json
from . import logic
from .models import LocalStore
import os
from django.conf import settings
import time

def index(request):
    if request.method == "POST":
        LocalStore.objects.all().delete()
        return render(request, "index.html")

    typeView = LocalStore.objects.all()
    if typeView.exists() == False:
        return render(request, "index.html")
    actor = typeView.last().actor

    if actor == "admin":
        return render(request, "admin/home.html")
    elif actor == "orgnaisation":
        applied=logic.getApplied('getComapanyApplied',typeView.last().userid)
    
        return render(request, "organisation/home.html",context={
            'applied':applied
        })
    elif actor == "user":
        data=logic.getTypeDiffer('getNameOfOrganisations',0)
        applied=logic.getApplied('getMyUserOrder',typeView.last().userid)
     
        return render(request, "users/home.html",context={
                'companies':data,
                 'applied':applied })
    else:
        return render(request, "index.html")


def submit(request):
    if request.method == "GET":
        name = request.GET.get("name", "")
        mobile = request.GET.get("mobile", "")
        email = request.GET.get("Email", "")
        password = request.GET.get("Password", "")
        adress = request.GET.get("Address", "")
        typeUser = request.GET.get("typeUser", "")
        lower = str(email).lower().strip()

        view = logic.userAdd(name, mobile, lower, password, adress, typeUser)
        print(view)
        return JsonResponse(data={"error": True, "message": view})


def login(request):
    if request.method == "GET":
        email = request.GET.get("email", "")
        password = request.GET.get("password", "")
        data = logic.loginSubmit(email, password)
        return JsonResponse(data={"error": True, "message": f"{data}"})


def adminPart(request):

    return render(request, "admin/home.html")


def viewOrgnisations(request):
    data = logic.getTypeDiffer("organisation",0)
    return render(request, "admin/view_orgnisation.html", context={"data": data})

def user(request):
    data=logic.getTypeDiffer('getNameOfOrganisations',0)
    return render(request,'users/home.html',context={
        'companies':data
    })

def organisation(request):
    return render(request,'organisation/home.html')

def uploadMyDetails(request):
    if request.method=="POST":
        drive=request.FILES['drive']
        photo=request.FILES['photo']
        addhaar=request.FILES['addhaar']
        companyId=request.POST.get("company","")
        fullName=request.POST.get("fullName","")
        motherName=request.POST.get("motherName","")
        adhaarNumber=request.POST.get("adhaarNumber","")
        panNumber=request.POST.get("panNumber","")



        first_millies=time.time_ns()// 1_000_000
        drivepath=os.path.join("app/static/savedImages/",f"{str(first_millies)}.jpg")
        with open(drivepath,"wb+") as destinationPort:
            for chunkPoint in drive.chunks():
                destinationPort.write(chunkPoint)
        drivepath=drivepath.replace("app/","/")
 
        second_milies=time.time_ns()// 1_000_000
        addhaarpath=os.path.join("app/static/savedImages/",f"{str(second_milies)}.jpg")
        with open(addhaarpath,"wb+") as destinationpathj:
            for chunkView in addhaar.chunks():
                destinationpathj.write(chunkView)
 
        addhaarpath=addhaarpath.replace("app/","/")

        third_millis=time.time_ns()// 1_000_000
        
        photopath=os.path.join("app/static/savedImages/",f"{str(third_millis)}.jpg")
        with open(photopath,"wb+") as destinationView:
            for chunkWay in photo.chunks():
                destinationView.write(chunkWay)

        photopath=photopath.replace("app/","/")
        
        userid=LocalStore.objects.all().last().userid
        appliedON=time.time_ns()// 1_000_000
        print(drivepath,addhaarpath,photopath)
        logic.addFileOF(companyId,userid,fullName,motherName,adhaarNumber,panNumber,drivepath,addhaarpath,photopath,str(appliedON))
        data=logic.getTypeDiffer('getNameOfOrganisations',0)

        applied=logic.getApplied('getMyUserOrder',userid)
     
        return render(request, "users/home.html",context={
                'companies':data,
                 'applied':applied })

    

def updatePoint(request):
    if request.method=="POST":
        id=request.POST.get("nameid",0)
        status=request.POST.get("status","")
        logic.updateStateOfContract(int(id),status)
        applied=logic.getApplied('getComapanyApplied',LocalStore.objects.all().last().userid)
    
        return render(request, "organisation/home.html",context={
            'applied':applied
        })
    
def profile(request):
    userID=LocalStore.objects.all().last().userid
    data=logic.getTypeDiffer("NothingUserProfile",userID)
    return render(request,'users/profile.html',context={
    'data':data
    })