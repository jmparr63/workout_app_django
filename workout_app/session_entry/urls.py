from django.urls import path

from . import views

urlpatterns = [
    # ex: /session_entry/
    path("", views.index, name="index"),
    # ex: /session_entry/index
    path("index", views.index, name="index"),
    # ex: /session_entry/capture
    path("capture", views.capture, name="capture"),
    path('cardio_form', views.get_cardio_form, name='get_cardio_form'),
    # ex: /session_entry/analyse
    path("analyse", views.analyse, name="analyse"),
    # ex: /session_entry/template
    path("template", views.template, name="template"),
    # ex: /session_entry/5/summary
    path("<int:session_id>/summary", views.summary, name="summary")
]