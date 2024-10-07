from django.urls import path

from . import views

urlpatterns = [
    # ex: /session_entry/
    path("", views.index, name="index"),
    # ex: /session_entry/5/summary
    path("<int:session_id>/summary", views.summary, name="summary")
]