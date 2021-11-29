from django.urls import path
from .views import onlyoneapp_vi

app_name = 'onlyoneapp'

urlpatterns = [
    path('view/',onlyoneapp_vi,name='view'),
]
