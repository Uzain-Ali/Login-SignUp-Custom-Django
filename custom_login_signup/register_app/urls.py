from . import views
from django.urls import path

urlpatterns = [
    path('register/',views.signup_view, name='register'),
]
