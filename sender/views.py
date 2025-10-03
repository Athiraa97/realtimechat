from django.shortcuts import render

def sender_view(request):
    return render(request, "sender/sender.html")
