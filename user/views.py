from django.db import connection
from django.shortcuts import render
from .form import Loginform, Drseform,addDrform,upDrform

from .models import Uer
from django.http import JsonResponse, HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def login(request):
    if request.method=="GET":
        print("1")
        return render(request,template_name="login.html")
    elif request.method=='POST':
        data=Loginform(request.POST)
        if data.is_valid():
            username=data.cleaned_data.get("username")
            password = data.cleaned_data.get("password")
            print(username)
            with connection.cursor() as cursor:
                cursor.execute("SELECT Pass_word ,is_staff FROM uer WHERE UserName = %s", [username])
                people=cursor.fetchone()
            print(people)
            if people!=None:
                if people[0]==password:
                    if people[1]==0:
                        return render(request,template_name='home.html')
                    else:
                        return render(request,template_name='staff_home.html')
                else:
                   return HttpResponse('密码错误')
            else:
                 return HttpResponse('无用户')
@csrf_exempt
def register(request):
    if request.method=="GET":
        return render(request,template_name="register.html")
    elif request.method=='POST':
        data=Loginform(request.POST)
        if data.is_valid():
            username=data.cleaned_data.get("username")
            password = data.cleaned_data.get("password")
            print(username)
            with connection.cursor() as cursor:
                cursor.execute("select * from Uer where UserName = %s", [username])
                people=cursor.fetchone()
                if people!=None:
                    return HttpResponse("该用户已存在")
                else:
                    cursor.execute("INSERT INTO Uer (UserName,Pass_word)VALUES (%s,%s);", [username,password])
                    return HttpResponse('插入成功')
@csrf_exempt
def Dr(request):
    if request.method=="GET":
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT 
            d.DrName AS '医生姓名',
            d.Gender AS '性别',
            d.Position AS '职位',
            d.About AS '专长描述',
            b.Bname AS '所属部门'
            FROM Dr d
            JOIN bumen b 
            ON d.BID = b.BID;""")
            data=cursor.fetchall()
            print(data)
            return render(request, template_name='Dr.html', context={"data": data})
    elif request.method == 'POST':
            print('1')
            data=Drseform(request.POST)
            if data.is_valid():
                name=data.cleaned_data.get("Drname")
                with connection.cursor() as cursor:
                    cursor.execute("""
                    SELECT *
                    FROM Dr
                    where DrName like %s
                    """ ,[name])
                    Dr=cursor.fetchall()
            print(Dr)

            return render(request,template_name='Dr.html',context={"data":Dr})
@csrf_exempt
def s_Dr(request):
    if request.method=="GET":
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT 
            d.DrName AS '医生姓名',
            d.Gender AS '性别',
            d.Position AS '职位',
            d.BirthDate AS '出生日期',
            d.Whentowork AS '上班时间',
            d.JoinDate AS '入职日期',
            d.Salary AS '薪资',
            d.About AS '专长描述',
            b.Bname AS '所属部门'
            FROM Dr d
            JOIN bumen b 
            ON d.BID = b.BID;""")
            data=cursor.fetchall()
            print(data)
            return render(request, template_name='s_Dr.html', context={"data": data})
    elif request.method == 'POST':
            print('1')
            data=Drseform(request.POST)
            if data.is_valid():
                name=data.cleaned_data.get("Drname")
                with connection.cursor() as cursor:
                    cursor.execute("""
                    SELECT *
                    FROM Dr
                    where DrName like %s
                    """ ,[name])
                    Dr=cursor.fetchall()
            print(Dr)

            return render(request,template_name='s_Dr.html',context={"data":Dr})
@csrf_exempt
def deDr(request):
    if request.method=='GET':
        return render(request,template_name='deDr.html')
    elif request.method == 'POST':
        data = Drseform(request.POST)
        if data.is_valid():
            name = data.cleaned_data.get("Drname")
            try:
                with connection.cursor() as cursor:
                    print(name)
                    cursor.execute("""
BEGIN TRANSACTION;

DECLARE @TargetDrID INT;
SELECT @TargetDrID = ID FROM Dr WHERE DrName = %s;

UPDATE Patient
SET DID = 16
WHERE DID = @TargetDrID;

DELETE FROM Dr
WHERE ID = @TargetDrID;

COMMIT TRANSACTION;
                    """, [name])
                return HttpResponse("删除成功")
            except:
                return HttpResponse('删除失败')

        else:
            print("dadwa")
            return HttpResponse('删除失败')
@csrf_exempt
def addDr(request):
    if request.method=='GET':
        return render(request,template_name='addDr.html')
    elif request.method == 'POST':
        data = addDrform(request.POST)
        if data.is_valid():
            name = data.cleaned_data.get("DrName")
            xb = data.cleaned_data.get("xb")
            ks = data.cleaned_data.get("ks")
            zw = data.cleaned_data.get("zw")
            sr = data.cleaned_data.get("sr")
            gzsj = data.cleaned_data.get("gzsj")
            jdwsj = data.cleaned_data.get("jdwsj")
            about = data.cleaned_data.get("about")
            qian = data.cleaned_data.get("qian")
            try:
                with connection.cursor() as cursor:
                    print(name)
                    cursor.execute("""
                        INSERT INTO Dr (
                        DrName,       
                        BID,           
                        Gender,
                        Position,
                        BirthDate,
                        Whentowork,
                        JoinDate,
                        salary,
                        About
          )
          VALUES (
          %s ,       
          (SELECT BID FROM bumen WHERE BName = %s),  
          %s,   
          %s, 
          %s, 
          %s, 
          %s, 
          %s, 
          %s    
                  );
                    """, [name,ks,xb,zw,sr,gzsj,jdwsj,qian,about])
                return HttpResponse("添加成功")
            except:
                return HttpResponse('添加失败')

        else:
            print("dadwa")
            return HttpResponse('添加失败')
@csrf_exempt
def upDr(request):
    if request.method=='GET':
        return render(request,template_name='upDr.html')
    elif request.method == 'POST':
        data = upDrform(request.POST)
        if data.is_valid():
            ID=data.cleaned_data.get('ID')
            name = data.cleaned_data.get("DrName")
            xb = data.cleaned_data.get("xb")
            ks = data.cleaned_data.get("ks")
            zw = data.cleaned_data.get("zw")
            sr = data.cleaned_data.get("sr")
            gzsj = data.cleaned_data.get("gzsj")
            jdwsj = data.cleaned_data.get("jdwsj")
            about = data.cleaned_data.get("about")
            qian = data.cleaned_data.get("qian")
            try:
                with connection.cursor() as cursor:
                    print([ID])
                    cursor.execute("""
                        UPDATE Dr
                        SET 
                        DrName = %s,
                        BID = (SELECT BID FROM bumen WHERE BName = %s),
                        Gender = %s,
                        Position = %s,
                        BirthDate = %s,
                        Whentowork = %s,
                        JoinDate = %s,
                        salary = %s,
                        About = %s
                        WHERE 
                        ID = %s;  
                    """, [name,ks,xb,zw,sr,gzsj,jdwsj,qian,about,ID])
                return HttpResponse("更新成功")
            except:
                return HttpResponse('更新失败')

        else:
            print("dadwa")
            return HttpResponse('更新失败')