from django.shortcuts import render

# Create your views here.
from functools import reduce


import math

import numpy 

import statistics


def home(request):

    result = "hanuma"

    return render(request,'home.html',{'result':result})

def add(request):

    
     
    val1 = request.GET['n1']
    list_val = list(map(int,val1.split(",")))

    


    if len(list_val) == 1:
        a = list_val[0]
    

    else:

        a = reduce(lambda a,b : a+b ,list_val)


    return render (request, 'home.html',{'res':a})

def sub(request):
    
    
    val1 = request.GET['n2']
    list_val = list(map(int,val1.split(",")))

    if len(list_val) == 1:
        s = list_val[0]
    

    else:

        s = reduce(lambda a,b : a-b ,list_val)

    return render (request, 'home.html',{'s':s})


def mul(request):

    val1 = request.GET['n3']
    list_val = list(map(int,val1.split(",")))

    if len(list_val) == 1:
        m = list_val[0]
    

    else:

        m = reduce(lambda a,b : a*b ,list_val)

    return render (request, 'home.html',{'m':m})

def div(request):

    
    val1 = request.GET['n4']
    list_val = list(map(int,val1.split(",")))

    if len(list_val) == 1:
        d = list_val[0]
    

    else:

        d = reduce(lambda a,b : a/b ,list_val)

        e = round(d,2)

    return render (request, 'home.html',{'d':e})

def lcm(request):

    val1 = request.GET['n5']
    list_val = list(map(int,val1.split(",")))

    if len(list_val) == 1:
        l = list_val[0]
    
    
    else:
        t = tuple(list_val)


        l = math.lcm(*t)

    return render (request, 'home.html',{'l':l})

    
def gcd(request):

    val1 = request.GET['n6']
    list_val = list(map(int,val1.split(",")))

    if len(list_val) == 1:
        g = list_val[0]
    
    
    else:
        t = tuple(list_val)


        g = math.gcd(*t)

    return render (request, 'home.html',{'g':g})

def fact(request):

    val1 = int(request.GET['n7'])
    


    f = math.factorial(val1)

    return render (request, 'home.html',{'f':f})

def fib(request):

    val1 = int(request.GET['n8'])

    if val1 <= 1:
        return  render (request, 'home.html',{'fi':val1})
    
    
    else :
        a = 0 
        b = 1 
        s = 0 
        for i in range(1,val1+1):
            s = a+b 
            b = a 
            a = s
        val1 = b
        

        return render (request, 'home.html',{'fi':val1})
    


def mean(request):

    val1 = request.GET['n9']
    list_val = list(map(int,val1.split(",")))

    


    me = numpy.mean(list_val)

    mean = round(me,3)

    return render (request, 'home.html',{'mean':mean})

    
def median(request):

    val1 = request.GET['n10']
    list_val = list(map(int,val1.split(",")))

    
       


    med = numpy.median(list_val)

    median = round(med,3)

    return render (request, 'home.html',{'median':median})


    
def mode(request):

    val1 = request.GET['n11']
    list_val = list(map(int,val1.split(",")))

   

    mod = statistics.mode(list_val)

        

    return render (request, 'home.html',{'mode':mod})


def std(request):

    val1 = request.GET['n12']
    list_val = list(map(int,val1.split(",")))

    


    s = numpy.std(list_val)

    std = round(s,3)

    return render (request, 'home.html',{'std':std})

def avg(request):

    val1 = request.GET['n13']
    list_val = list(map(int,val1.split(",")))

    a = sum(list_val)/len(list_val)

    avg = round(a,3)


    return render (request, 'home.html',{'avg':avg})


def power(request):

    val1 = request.GET['n14']
    list_val = list(map(int,val1.split(",")))

    p = list_val[0] ** list_val[1]

    return render (request, 'home.html',{'pwr':p})