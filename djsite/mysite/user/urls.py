from django.urls import path
from user.views import login_view, registration_view

urlpatterns = [
    path("login/", login_view, name='login'),
    path("registration/", registration_view, name='registration')
]