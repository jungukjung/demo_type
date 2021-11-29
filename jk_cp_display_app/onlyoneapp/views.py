from django.shortcuts import render

# Create your views here.

def onlyoneapp_vi(request):

    context ={}

    return render(request,'onlyoneapp/view.html',context)
