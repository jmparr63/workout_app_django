from django.http import HttpResponse
from django.template import loader

from .models import Session

def index(request):
    latest_session_list = [s.date.strftime('%a %d %b %Y, %I:%M%p') for s in Session.objects.order_by("-date")[:5]]
    template = loader.get_template("session_entry/index.html")
    context = {
        "latest_session_list": latest_session_list,
    }
    return HttpResponse(template.render(context, request))

def summary(request, session_id):
    response = "You're looking at the results of session %s"
    return HttpResponse(response % session_id)