from django.urls import path
from accounts.views import register_view, MyLogoutView
from django.contrib.auth.views import LoginView


app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('create/', register_view, name='create'),
]

