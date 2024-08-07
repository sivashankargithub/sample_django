from django.shortcuts import render
from app1.models import students
from app1.forms import studentform1

def home1(request):
    if request.method=='POST':
        form1=studentform1(request.POST)
        if form1.is_valid():
            form1.save()
            return render(request,'app1/index.html',{'form':form1,'param1':'Success'})
    else:
        form1=studentform1()
    return render(request,'app1/index.html',{'form':form1})
