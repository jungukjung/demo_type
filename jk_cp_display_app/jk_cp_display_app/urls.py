from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('total_view_app/',include("total_view_app.urls"),name='total_view_app'),
]
