from django.shortcuts import render
from app1.forms import inputform1

def factorial1(num1):
    fact1=1
    for i in range(1,num1+1,1):
        fact1=fact1*i
    return fact1

def square(num1):
    return num1*num1

def home1(request):
    if request.method=="POST":
        form1=inputform1(request.POST)
        if form1.is_valid():
            data1=form1.cleaned_data
            num1=data1.get('input1')
            result1=square(num1)
            result2=factorial1(num1)
            return render(request,'app1/index.html',
                {'param1':num1,'param2':result1,'param3':result2,'form':form1})
    else:
        form1=inputform1()
    return render(request,'app1/index.html',{'form':form1})