from django.contrib import admin

from .models import Session, ResistanceExercise, CardioExercise

admin.site.register(Session)
admin.site.register(ResistanceExercise)
admin.site.register(CardioExercise)