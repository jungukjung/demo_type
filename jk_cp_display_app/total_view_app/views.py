from django.shortcuts import render

# Create your views here.

def total_view_app_vi(request):

    context ={}

    return render(request,'total_view_app/view.html',context)
