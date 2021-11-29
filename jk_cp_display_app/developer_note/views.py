from django.shortcuts import render

# Create your views here.
def developer_note_vi(request):

    context ={}

    return render(request,'developer_note/view.html',context)