from django.urls import path
from . import views

urlpatterns = [
    path("", views.receiver_view, name="receiver"),
]
