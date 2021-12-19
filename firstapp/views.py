from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from firstapp.models import Exam,Login,Registration,UploadImage

# Create your views here.

def ExamPage(request):
    if request.method == 'POST':
        name1 = request.POST.get("n1")
        age1 = request.POST.get("a1")
        # name = request.POST["n1"]
        obj = Exam()
        obj.name = name1
        obj.age = age1
        obj.save()
        context = {'n': name1, 'a': age1}
        return render(request, 'exam.html', context)
    return render(request, 'exam.html')

def viewDetails(request):
    exm = Exam.objects.all() #select * from table
    context = {'exm':exm}
    return render(request,"viewdetails.html",context)

def editDetails(request,id):
    edit = Exam.objects.get(id=id) #select * from table where id='id'
    return render(request,'editdetails.html',{'edit':edit})

def update(request,id):
    name1 = request.POST.get("n1")
    age1 = request.POST.get("a1")
    # name = request.POST["n1"]
    obj = Exam.objects.get(id=id)
    obj.name = name1
    obj.age = age1
    obj.save()
    return redirect("viewdetails")

def deleteDetails(request,id):
    obj = Exam.objects.get(id=id)
    obj.delete() #Delete details from db
    return redirect('viewdetails')
   # return HttpResponse("<script>alert('successfully deleted');window.location='/examapp/viewdetails';</script>")

#views for login and registration pages
def registerPage(request):
    return render(request,'LogReg/register.html')

def loginPage(request):
    return render(request,'LogReg/login.html')

def registerProcess(request):
    fname = request.POST.get('fullname')
    mail = request.POST.get('email')
    gender = request.POST.get('gender')
    mob = request.POST.get('mob')
    category = request.POST.get('category')
    uname = request.POST.get('uname')
    pswd = request.POST.get('pass')

    log = Login()
    log.username = uname
    log.password = pswd
    log.role = "user"
    log.save()

    reg = Registration()
    reg.Fullname = fname
    reg.Email = mail
    reg.Gender = gender
    reg.mobile = mob
    reg.Category = category
    reg.login = log # select max(id) from login
    reg.save()
    return HttpResponse("<script>alert('successfully register...login now');window.location='/firstapp/login';</script>")

def loginProcess(request):
    uname = request.POST.get('uname')
    pswd = request.POST.get('pass')
    if Login.objects.filter(username=uname, password=pswd).exists():
        loginobj = Login.objects.get(username=uname, password=pswd)
        request.session['loginid'] = loginobj.id
        request.session['uname'] = loginobj.username
        role = loginobj.role

        if (role == "admin"):
            return redirect("AdminHome")
            #return HttpResponse("welcome admin")
        elif (role == "user"):
            return redirect("UserHome")
            #return HttpResponse("welcome user")
        else:
            return HttpResponse("<script>alert('login failed...try again');window.location='/firstapp/login';</script>")

    else:
        return HttpResponse("<script>alert('invalid username and password...try again');window.location='/firstapp/login';</script>")

def AdminHome(request):
    logid = request.session.get('loginid')
    adm = Registration.objects.get(login_id=logid)
    return render(request,'admin/adminhome.html',{'adm':adm})

def UserHome(request):
    logid = request.session.get('loginid')
    adm = Registration.objects.get(login_id=logid)
    return render(request,'user/userhome.html',{'adm':adm})

def logout1(request):
    logout(request)
    return HttpResponse("<script>alert('you are successfully Logged off..');window.location ='/firstapp/login';</script>")

def imagePage(request):
    return render(request,'user/imageupload.html')

def imageProcess(request):
    logid = request.session.get('loginid')
    upimage = request.FILES.get('image')
    up = UploadImage()
    up.imagename = upimage
    up.login = logid
    up.save()
    return redirect('image')
