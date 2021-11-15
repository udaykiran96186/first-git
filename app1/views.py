from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect

def home(request):
    return HttpResponse("<h1>Hello World!</h1>")

def hello(request):
    return HttpResponseRedirect('/app1')
    # return redirect(home)

def joker(request):
    return render(request,"joker.html")