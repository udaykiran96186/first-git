from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from app1.forms import StudentForm
from app1.models import Student

def home(request):
    return HttpResponse("<h1>Hello World!</h1>")

def hello(request):
    return HttpResponseRedirect('/app1')
    # return redirect(home)

def joker(request):
    context = {'a':10,
                'list':[10,20,30.5],
                'str':'it is a string',
            }
    return render(request,"joker.html",context)

def getData(request):
    allData = Student.objects.all()
    context = {
        'allData':allData
    }
    return render(request,"get.html",context)

def getName(request):
    nameData = Student.objects.all().values("name")
    context = {
        "nameData":nameData
    }
    return render(request,"show.html",context)

def get(request,id):
    oneData = Student.objects.get(id=id)
    context = {
        "oneData":oneData
    }
    return HttpResponse(f"name is {oneData.name} with phone number {oneData.phone} and address is {oneData.address}")


def formView(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(formView)

    context = {
        "form":form
    }
    return render(request,"form.html",context)

def formHtml(request):
    if request.method == "POST":
        fname = request.POST.get("name")
        fphone = request.POST.get("phone")
        faddress = request.POST.get("address")
        a = Student.objects.create(name=fname,address=faddress,phone=fphone)
        a.save()
        return redirect(formHtml)
    return render(request,"formHtml.html")