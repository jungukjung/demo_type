from django.shortcuts import render

# Create your views here.
def error_tips_app_vi(request):

    context ={}

    return render(request,'error_tips_app/view.html',context)