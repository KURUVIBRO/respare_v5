from django.shortcuts import render

# Create your views here.
def topic(request,pk):
    return render(request,'topic.html',{'id':pk})