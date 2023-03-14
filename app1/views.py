from django.shortcuts import render

# Create your views here.
def hari(request):
    d={'a':10,'b':20,'c':30}
    return render(request,'hari.html',context=d)