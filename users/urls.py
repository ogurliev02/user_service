from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserView.as_view()),
    path('user/', EmailView.as_view()),
]