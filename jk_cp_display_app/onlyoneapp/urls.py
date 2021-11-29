from django.urls import path
from .views import total_view_app_vi

app_name = 'total_view_app'

urlpatterns = [
    path('view/',total_view_app_vi,name='view'),
]
