from django.urls import path
from .views import developer_note_vi

app_name = 'developer_note'

urlpatterns = [
    path('view/',developer_note_vi,name='view'),
]
