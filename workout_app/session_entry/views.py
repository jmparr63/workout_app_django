from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Session

def index(request):
    latest_session_list = [s.date.strftime('%a %d %b %Y, %I:%M%p') for s in Session.objects.order_by("-date")[:5]]
    template = loader.get_template("session_entry/index.html")
    context = {
        "latest_session_list": latest_session_list,
    }
    return render(request, "session_entry/index.html", context)

def summary(request, session_id):
    response = "You're looking at the results of session %s"
    return HttpResponse(response % session_id)

def capture(request):
    return render(request, "session_entry/capture.html")

def analyse(request):
    return render(request, "session_entry/analyse.html")

def template(request):
    return render(request, "session_entry/template.html")
