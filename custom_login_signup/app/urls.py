from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.home,name="home"),
    path('login/',views.login_view, name='login'),
    path('register/',views.signup_view, name='register'),
    path('logout/', views.logout_view, name='logout')
]
