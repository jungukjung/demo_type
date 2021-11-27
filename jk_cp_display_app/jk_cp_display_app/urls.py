from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from total_view_app.views import total_view_app_vi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',total_view_app_vi,name='view'),
    path('total_view_app/',include("total_view_app.urls"),name='total_view_app'),
]
