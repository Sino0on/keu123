from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('discipline/<int:pk>', disciplines, name='discipline_detail'),
]