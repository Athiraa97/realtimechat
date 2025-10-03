from django.shortcuts import render

def receiver_view(request):
    return render(request, "receiver/receiver.html")
