from django.urls import path
from . import views

urlpatterns = [
    path("", views.sender_view, name="sender"),
]
