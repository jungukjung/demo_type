from django.shortcuts import render

# Create your views here.

def plannerapp_vi(request):

    context ={}

    return render(request,'plannerapp/view.html',context)