from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from onlyoneapp.views import onlyoneapp_vi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',onlyoneapp_vi,name='view'),
    
    
    path('onlyoneapp/',include("onlyoneapp.urls"),name='onlyoneapp'),
    path('plannerapp/',include("plannerapp.urls"),name='plannerapp'),
    path('error_tips_app/',include("error_tips_app.urls"),name='error_tips_app'),
    path('developer_note/',include("developer_note.urls"),name='developer_note'),
]
