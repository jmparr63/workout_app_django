from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Button, HTML
from crispy_forms.bootstrap import FormActions

class CardioExerciseForm(forms.Form):
    CARDIO_CHOICES = [
        ('running', 'Running'),
        ('cycling', 'Cycling'),
        ('swimming', 'Swimming'),
        ('other', 'Other'),
    ]
    
    cardio_type = forms.ChoiceField(choices=CARDIO_CHOICES)
    distance = forms.FloatField(label='Distance (km)', min_value=0, initial=1, step_size=0.1)
    resistance = forms.IntegerField(label='Resistance/Incline level', required=False, min_value=0)
    notes = forms.CharField(widget=forms.TextInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('cardio_type'),
            Field('distance'),
            Field('resistance'),
            Field('notes'),
            HTML("<hr>")
        )

class WorkoutForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('date'),
            HTML("<div id='cardio-exercises'></div>"),
            Button('add-cardio', 'Add Cardio Exercise', css_class='btn btn-secondary', css_id='add-cardio-btn'),
            FormActions(
                Button('submit', 'Save Workout', css_class='btn special')
            )
        )