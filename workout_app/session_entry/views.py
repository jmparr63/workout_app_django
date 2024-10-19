from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.template.loader import render_to_string


from .models import Session
from .forms import WorkoutForm, CardioExerciseForm


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
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            # Process the form data
            # You'll need to iterate through the formsets to access all the data
            pass
    else:
        form = WorkoutForm()

    return render(request, "session_entry/capture.html", {'form': form})

def get_cardio_form(request):
    form_index = request.GET.get('form_index')
    cardio_form = CardioExerciseForm(prefix=f'{form_index}')
    context = {'form': cardio_form}
    html = render_to_string('session_entry/cardio_form.html', context)
    return HttpResponse(html)




def analyse(request):
    return render(request, "session_entry/analyse.html")

def template(request):
    return render(request, "session_entry/template.html")
