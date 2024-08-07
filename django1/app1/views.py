from django.shortcuts import render

def home(request):
    num1=5
    result1=square(num1)
    result2=factorial1(num1)
    return render(request,'app1/index.html',
                  {'param1':num1,'param2':result1,'param3':result2})


def square(num1):
    return num1*num1

def factorial1(num1):
    fact1=1
    for i in range(1,num1+1,1):
        fact1=fact1*i
    return fact1