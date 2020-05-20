# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages
from app.models import *


@login_required(login_url="/login/")
def index(request):
    return render(request, "index.html")

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        if request.method == "POST":
            load_template(request)
        template = loader.get_template('pages/' + load_template)
        return HttpResponse(template.render(context, request))

    except:

        template = loader.get_template( 'pages/error-404.html' )
        return HttpResponse(template.render(context, request))

def idcard_form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        employment_id = request.POST.get('employment_id')
        customer_account_number= request.POST.get('customer_account_number')
        circle= request.POST.get('circle')
        company_name= request.POST.get('company_name')
        department= request.POST.get('department')
        certificate_number= request.POST.get('certificate_number')
        date= request.POST.get('date')
        idcard1 = idcard(name=name,employment_id=employment_id,customer_account_no=customer_account_number,circle=circle,company_name=company_name,department=department,certificate_no=certificate_number,date=date)
        idcard1.save()
        messages.success(request,"Your data has been submiteed successfully!!")
        return render(request,'pages/idcard-form.html',context=None)
    else:
        return render(request,'pages/idcard-form.html',context=None)


def certificate_form(request):
    if request.method=="POST":
        name=request.POST.get('name')
        training_name=request.POST.get('training_name')
        certificate_validity=request.POST.get('certificate_validity')
        date=request.POST.get('date')
        place=request.POST.get('place')
        print("Place is "+place)
        certificate=Certificate(name=name,training_name=training_name,certificate_validity=certificate_validity,date=date,place=place)
        certificate.save()
        messages.success(request,"Your data has been submiteed successfully!!")
    return render(request,'pages/certificate_form.html',context=None)
    #return HttpResponse("Hello I am certificate")

def certificate_verification(request):
    return render(request,'pages/certificate-verification.html')
def printreport(request):
    report = Report.objects.all()
    return render(request,'pages/printreport.html',{'report':report})

def reportform(request):
    if request.method=="POST":
        name=request.POST.get('name')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        dob=request.POST.get('dob')
        email=request.POST.get('email')
        q1=request.POST.get('q1')
        q2=request.POST.get('q2')
        q3=request.POST.get('q3')
        q4=request.POST.get('q4')
        q5=request.POST.get('q5')
        q6=request.POST.get('q6')
        q7=request.POST.get('q7')
        q8=request.POST.get('q8')
        q9=request.POST.get('q9')
        q10=request.POST.get('q10')
        q11=request.POST.get('q11')
        image=""
        comment=request.POST.get('comment')
        height=request.POST.get('height')
        weight=request.POST.get('weight')
        systolic=request.POST.get('systolic')
        diastolic=request.POST.get('diastolic')
        pulserate=request.POST.get('pulserate')
        heartsound=request.POST.get('heartsound')
        peripheralpulse=request.POST.get('peripheralpulse')
        chestlung=request.POST.get('chestlung')
        curvicalspine=request.POST.get('curvicalspine')
        backmovements=request.POST.get('backmovements')
        upperlimbs=request.POST.get('upperlimbs')
        jointmovements=request.POST.get('jointmovements')
        reflexes=request.POST.get('reflexes')
        rombergs=request.POST.get('rombergs')
        hearing=request.POST.get('hearing')
        vision=request.POST.get('vision')
        albumin=request.POST.get('albumin')
        sugar=request.POST.get('sugar')
        blood_group=request.POST.get('blood_group')
        rh_factor=request.POST.get('rh_factor')
        hb=request.POST.get('hb')
        tlc=request.POST.get('tlc')
        rbc=request.POST.get('rbc')
        plateletscount=request.POST.get('plateletscount')
        triglycerides=request.POST.get('triglycerides')
        hdl=request.POST.get('hdl')
        ldl=request.POST.get('ldl')
        result=request.POST.get('result')
        registration_no=request.POST.get('registration_no')
        date_of_examination=request.POST.get('date_of_examination')
        report=Report(name=name,gender=gender, address= address,dob=dob,email=email,q1=q1,q2=q2,q3=q3,q4=q4,q5=q5,q6=q6,q7=q7,q8=q8,q9=q9,q10=q10,q11=q11,image=image,comment=comment,height=height,weight=weight,systolic=systolic,diastolic=diastolic,pulserate=pulserate,heartsound=heartsound,peripheralpulse=peripheralpulse,chestlung=chestlung,curvicalspine=curvicalspine,backmovements=backmovements,upperlimbs=upperlimbs,jointmovements=jointmovements,reflexes=reflexes,rombergs=rombergs,hearing=hearing,vision=vision,albumin=albumin,sugar=sugar,blood_group=blood_group,rh_factor=rh_factor,hb=hb,tlc=tlc,rbc=rbc,plateletscount=plateletscount,triglycerides=triglycerides,hdl=hdl,ldl=ldl,result=result,registration_no=registration_no,date_of_examination=date_of_examination)
        report.save()
        messages.success(request,"Your data has been submiteed successfully!!")
    return render(request,'pages/reportform.html',context=None)
    

