from django.shortcuts import render
from app1.forms import InputForm1
from random import randint

range1=100
randnum1=randint(0,range1)
def home1(request):
    msg1=""
    in1=range1+1
    if request.method=='POST':
        form1=InputForm1(request.POST)
        if form1.is_valid():
            data1=form1.cleaned_data
            while in1!=randnum1:
                in1=data1.get("input1")
                if in1==randnum1:
                    msg1="Your Guess is Correct. It is "+str(randnum1)
                if in1<randnum1:
                    msg1="Enter Bigger Number than this "
                if in1>randnum1:
                    msg1="Enter Smaller Number than this "
                return render(request,'app1/index.html',{'form':form1,'param1':msg1})
    else:
        form1=InputForm1()
    return render(request,'app1/index.html',{'form':form1})
