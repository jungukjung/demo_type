from django.urls import path
from .views import plannerapp_vi

app_name = 'plannerapp'

urlpatterns = [
    path('view/',plannerapp_vi,name='view'),
]
