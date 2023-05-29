from django.shortcuts import render,redirect
from.forms import todoform
from.models import login
# Create your views here.
def fun(request):
    form=todoform()
    t=login.objects.all()
    if request.method=='POST':
        form=todoform(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'register.html',{'fo':form,'todo':t})


    