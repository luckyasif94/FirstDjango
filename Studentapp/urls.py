from django.urls import path
from . import views

urlpatterns = [
    path('studenthome/<int:a>',views.index)
]
