from django.shortcuts import render
from app1.forms import inputform1

def square(start,end):
    list1=[]
    list2=[]
    list3=[]
    for i in range(start,end+1,1):
        list1.append(i)
        list2.append(i*i)
    list3=zip(list1,list2)
    return list3

def factorial1(start,end):
    list1=[]
    list2=[]
    list3=[]
    for i in range(start,end+1,1):
        fact1=1
        list1.append(i)
        for j in range(1,i+1,1):
            fact1=fact1*j
        list2.append(fact1)
    list3=zip(list1,list2)
    return list3

def home1(request):
    if request.method=='POST':
        form1=inputform1(request.POST)
        if form1.is_valid():
            data1=form1.cleaned_data
            start1=data1.get('input1')
            end1=data1.get('input2')
            result1=square(start1,end1)
            result2=factorial1(start1,end1)
            return render(request,'app1/index.html',{'param1':result1,'param2':result2,'form':form1})
    else:
        form1=inputform1()
    return render(request,'app1/index.html',{'form':form1})
