from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from patient.form import pasefrom
from .form import segjform,semeform,addmeform,upmeform,addgjform,upgjform

# Create your views here.
@csrf_exempt
def s_gongju(request):
    if request.method=='GET':
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT *
            FROM gongju""")
            data=cursor.fetchall()
            print(data)

        return render(request,template_name='s_gongju.html',context={"data":data})
    elif request.method == 'POST':
            print('1')
            data=segjform(request.POST)
            if data.is_valid():
                name=data.cleaned_data.get("GName")
                with connection.cursor() as cursor:
                    print(name)
                    cursor.execute("""
                    SELECT *
                    FROM gongju
                    where GName like %s
                    """ ,[name])
                    pa=cursor.fetchall()
                    print(pa)
            else:
                print("dadwa")


            return render(request,template_name='s_gongju.html',context={"data":pa})
@csrf_exempt
def s_med(request):
    if request.method=='GET':
        with connection.cursor() as cursor:
            cursor.execute("""SELECT 
    m.*,
    d.name AS pharmacy_name  
FROM 
    Medicine m  
LEFT JOIN 
    med_ku d ON m.kid = d.id  
""")
            data=cursor.fetchall()
            print(data)

        return render(request,template_name='s_med.html',context={"data":data})
    elif request.method == 'POST':
            print('1')
            data=semeform(request.POST)
            if data.is_valid():
                name=data.cleaned_data.get("MName")
                with connection.cursor() as cursor:
                    print(name)
                    cursor.execute("""
                             SELECT 
    m.*,
    d.name AS pharmacy_name  
FROM 
    Medicine m  
LEFT JOIN 
    med_ku d ON m.kid = d.id  -- 关联科室表(假设科室表包含药房信息)
where m.MName like %s
                    """ ,[name])
                    pa=cursor.fetchall()
                    print(pa)
            else:
                print("dadwa")

            return render(request,template_name='s_med.html',context={"data":pa})
@csrf_exempt
def deme(request):
    if request.method=='GET':
        return render(request,template_name='deme.html')
    elif request.method == 'POST':
        data = semeform(request.POST)
        if data.is_valid():
            name = data.cleaned_data.get("MName")
            try:
                with connection.cursor() as cursor:
                    print(name)
                    cursor.execute("""
                    DELETE FROM Medicine
                    WHERE MName = %s;  
                    """, [name])
                return HttpResponse("删除成功")
            except:
                return HttpResponse('删除失败')

        else:
            print("dadwa")
            return HttpResponse('删除失败')

@csrf_exempt
def addme(request):
    if request.method=='GET':
        return render(request,template_name='addme.html')
    elif request.method == 'POST':
        data = addmeform(request.POST)
        if data.is_valid():
            name = data.cleaned_data.get("MName")
            Many = data.cleaned_data.get("Many")
            price = data.cleaned_data.get("Price")
            About = data.cleaned_data.get("About")
            try:
                with connection.cursor() as cursor:
                    print(name)
                    cursor.execute("""
                    INSERT INTO Medicine(MName,Price,Many,About)
                    VALUES (%s,%s,%s,%s)
                    """, [name,Many,price,About])
                return HttpResponse("添加成功")
            except:
                return HttpResponse('添加失败')

        else:
            print("dadwa")
            return HttpResponse('添加失败')

@csrf_exempt
def upme(request):
    if request.method=='GET':
        return render(request,template_name='upme.html')
    elif request.method == 'POST':
        data = upmeform(request.POST)
        if data.is_valid():
            ID=data.cleaned_data.get("ID")
            name = data.cleaned_data.get("MName")
            Many = data.cleaned_data.get("Many")
            price = data.cleaned_data.get("Price")
            About = data.cleaned_data.get("About")
            try:
                with connection.cursor() as cursor:
                    print(name)
                    cursor.execute("""
                    UPDATE Medicine
                    SET
                        MName= %s,
                        Many= %s,
                        Price = %s,
                        About = %s
                    where ID=%s
                    """, [name,Many,price,About,ID])
                return HttpResponse("添加成功")
            except:
                return HttpResponse('添加失败')

        else:
            print("dadwa")
            return HttpResponse('添加失败')
@csrf_exempt
def addgj(request):
    if request.method=='GET':
        return render(request,template_name='addgj.html')
    elif request.method == 'POST':
        data = addgjform(request.POST)
        if data.is_valid():
            name = data.cleaned_data.get("GName")
            Many = data.cleaned_data.get("Many")
            price = data.cleaned_data.get("Price")
            About = data.cleaned_data.get("About")
            try:
                with connection.cursor() as cursor:
                    print(name)
                    cursor.execute("""
                    INSERT INTO gongju(GName,Price,Many,About)
                    VALUES (%s,%s,%s,%s)
                    """, [name,Many,price,About])
                return HttpResponse("添加成功")
            except:
                return HttpResponse('添加失败')

        else:
            print("dadwa")
            return HttpResponse('添加失败')
@csrf_exempt
def degj(request):
    if request.method=='GET':
        return render(request,template_name='degj.html')
    elif request.method == 'POST':
        data = segjform(request.POST)
        if data.is_valid():
            name = data.cleaned_data.get("GName")
            try:
                with connection.cursor() as cursor:
                    print(name)
                    cursor.execute("""
                    DELETE FROM gongju
                    WHERE GName = %s;  
                    """, [name])
                return HttpResponse("删除成功")
            except:
                return HttpResponse('删除失败')

        else:
            print("dadwa")
            return HttpResponse('删除失败')
@csrf_exempt
def upgj(request):
    if request.method=='GET':
        return render(request,template_name='upgj.html')
    elif request.method == 'POST':
        data = upgjform(request.POST)
        if data.is_valid():
            ID=data.cleaned_data.get("ID")
            name = data.cleaned_data.get("GName")
            Many = data.cleaned_data.get("Many")
            price = data.cleaned_data.get("Price")
            About = data.cleaned_data.get("About")
            try:
                with connection.cursor() as cursor:
                    print(name)
                    cursor.execute("""
                    UPDATE gongju
                    SET
                        GName= %s,
                        Many= %s,
                        Price = %s,
                        About = %s
                    where ID=%s
                    """, [name,Many,price,About,ID])
                return HttpResponse("添加成功")
            except:
                return HttpResponse('添加失败')

        else:
            print("dadwa")
            return HttpResponse('添加失败')