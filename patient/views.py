from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .form import pasefrom,addpafrom,uppafrom
from datetime import datetime

# Create your views here.
@csrf_exempt
def patient(request):
    if request.method=="GET":
        with connection.cursor() as cursor:
            cursor.execute("""
                        SELECT 
                        p.*,
                        d.DrName AS doctor_name
                        FROM 
                        patient p
                        LEFT JOIN 
                        Dr d ON p.DID = d.ID
            where IsDischarged = 0""")
            data=cursor.fetchall()
            print(data)

        return render(request,template_name='patient.html',context={"data":data})
    elif request.method == 'POST':
            print('1')
            data=pasefrom(request.POST)
            if data.is_valid():
                name=data.cleaned_data.get("PaName")
                with connection.cursor() as cursor:
                    cursor.execute("""
                    SELECT *
                    FROM patient
                    where PName like %s
                    """ ,[name])
                    pa=cursor.fetchall()
                    print(pa)
            else:
                print("dadwa")


            return render(request,template_name='patient.html',context={"data":pa})
@csrf_exempt
def s_patient(request):
    if request.method=="GET":
        with connection.cursor() as cursor:
            cursor.execute("""
                        SELECT 
                        p.*,
                        d.DrName AS doctor_name
                        FROM 
                        patient p
                        LEFT JOIN 
                        Dr d ON p.DID = d.ID""")
            data=cursor.fetchall()
            print(data)

        return render(request,template_name='s_patient.html',context={"data":data})
    elif request.method == 'POST':
            print('1')
            data=pasefrom(request.POST)
            if data.is_valid():
                name=data.cleaned_data.get("PaName")
                with connection.cursor() as cursor:
                    cursor.execute("""
SELECT 
    p.*,
    d.DrName AS doctor_name
FROM 
    patient p
LEFT JOIN 
    Dr d ON p.DID = d.ID
                    where PName like %s
                    """ ,[name])
                    pa=cursor.fetchall()
                    print(pa)
            else:
                print("dadwa")


            return render(request,template_name='s_patient.html',context={"data":pa})
@csrf_exempt
def bed(request):
    if request.method=="GET":
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT 
    b.RoomNumber AS 病房号,
    b.BedNumber AS 床位号,
    k.KName AS 科室名称
FROM 
    Bed b
JOIN 
    keshi k ON b.KID = k.KID  
WHERE 
    b.onuser = 0;  -- 筛选未占用的床位""")
            data=cursor.fetchall()
            print(data)

        return render(request,template_name='bed.html',context={"data":data})
@csrf_exempt
def s_bed(request):
    if request.method=="GET":
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT 
    b.RoomNumber AS 病房号,
    b.BedNumber AS 床位号,
    b.onuser,
    k.KName AS 科室名称
FROM 
    Bed b
JOIN 
    keshi k ON b.KID = k.KID  -- 通过 KID 关联科室表
  -- 筛选未占用的床位""")
            data=cursor.fetchall()
            print(data)

        return render(request,template_name='s_bed.html',context={"data":data})
@csrf_exempt
def depa(request):
    if request.method=="GET":
        return render(request,template_name='depa.html')
    elif request.method == 'POST':
            print('1')
            data=pasefrom(request.POST)
            if data.is_valid():
                name=data.cleaned_data.get("PaName")
                print(name)
                try:
                    with connection.cursor() as cursor:
                        cursor.execute("""
                        UPDATE PATIENT
                        SET
                            IsDischarged='True'
                        where PName = %s
                        """ ,[name])
                        return HttpResponse("出院成功")
                except:
                    return HttpResponse('出院失败')

            else:
                print("dadwa")
                return HttpResponse('出院失败')
@csrf_exempt
def addpa(request):
    if request.method=='GET':
        return render(request,template_name='addpa.html')
    elif request.method == 'POST':
        data = addpafrom(request.POST)
        if data.is_valid():
            name = data.cleaned_data.get("PaName")
            xingbie = data.cleaned_data.get("Gender")
            keshi = data.cleaned_data.get("KName")
            about=data.cleaned_data.get('Condition')
            Dr = data.cleaned_data.get("Dr")
            BID = data.cleaned_data.get("BID")
            time=datetime.now()
            print(name, xingbie,keshi,Dr,BID,about)
            print(time)

            try:
                with connection.cursor() as cursor:
                    print(name)
                    cursor.execute("""
                    INSERT INTO patient (
                        PName,        
                        Gender,
                        Condition,
                        PDate,
                        BID,
                        DID,           
                        KID            
                        )
                        SELECT 
                        %s,    
                        %s,
                        %s,
                        %s,
                        %s,
                        d.ID,         
                        dp.KID        
                        FROM 
                        Dr d,          
                        keshi dp          
                        WHERE 
                            d.DrName = %s  
                            AND dp.KName = %s; 
                    """,[name,xingbie,about,time,BID,Dr,keshi])
                return HttpResponse("插入成功")
            except:
                return HttpResponse('插入失败')

        else:
            print("dadwa")
            return HttpResponse('插入失败')
@csrf_exempt
def uppa(request):
    if request.method=='GET':
        return render(request,template_name='uppa.html')
    elif request.method == 'POST':
        data = uppafrom(request.POST)
        if data.is_valid():
            ID=data.cleaned_data.get('ID')
            name = data.cleaned_data.get("PaName")
            xingbie = data.cleaned_data.get("Gender")
            keshi = data.cleaned_data.get("KName")
            about=data.cleaned_data.get('Condition')
            Dr = data.cleaned_data.get("Dr")
            BID = data.cleaned_data.get("BID")
            time=datetime.now()
            print(ID,name, xingbie,keshi,Dr,BID,about)
            print(time)

            try:
                with connection.cursor() as cursor:
                    print(name)
                    cursor.execute("""
                    UPDATE patient
                    SET 
                    PName = %s,
                    Gender = %s,
                    Condition = %s,
                    PDate = %s,
                    BID = %s,
                    DID = (SELECT d.ID FROM Dr d WHERE d.DrName = %s),  
                    KID = (SELECT dp.KID FROM keshi dp WHERE dp.KName = %s)  
                    WHERE 
                    ID = %s;  
                    """,[name,xingbie,about,time,BID,Dr,keshi,ID])
                return HttpResponse("更新成功")
            except:
                return HttpResponse('更新失败')

        else:
            print("dadwa")
            return HttpResponse('gengx失败')