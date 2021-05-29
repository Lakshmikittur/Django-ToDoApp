from django.urls import path
from .views import (
    register_view, 
    profile_view,
)

app_name = "users"
urlpatterns = [
    path('register/', register_view, name="registeruser"),
    path('profile/', profile_view, name='profile'),
]