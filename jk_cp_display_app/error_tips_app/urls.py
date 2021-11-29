from django.urls import path
from .views import error_tips_app_vi

app_name = 'error_tips_app'

urlpatterns = [
    path('view/',error_tips_app_vi,name='view'),
]
