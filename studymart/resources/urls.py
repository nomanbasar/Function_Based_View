from django.urls import path
from . import views

urlpatterns = [
    path('fc/',views.Free_course),
    path('bg/',views.blog),
    
]