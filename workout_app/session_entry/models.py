from django.db import models

class Session(models.Model):
    date = models.DateTimeField("date of session")

    class Meta:
        db_table = "session"
        
    def __str__(self):
        return f"{self.date.strftime('%a %d %b %Y, %I:%M%p')}"


class ResistanceExercise(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    muscle_group = models.CharField(max_length=100)
    
    class Meta:
        db_table = "resistance_exercise"

    def __str__(self):
        return self.name


class ResistanceSet(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    resist_ex = models.ForeignKey(ResistanceExercise, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    reps = models.IntegerField(default=8)
    notes = models.CharField(max_length=1000)

    class Meta:
        db_table = "resistance_set"

    def __str__(self):
        return f"Weight: {self.weight}kg Reps: {self.reps}"


class CardioExercise(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "cardio_exercise"

    def __str__(self):
        return self.name


class CardioActivity(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    cardio_ex = models.ForeignKey(CardioExercise, on_delete=models.CASCADE)
    distance = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.DurationField()
    resistance = models.IntegerField(default=0)
    notes = models.CharField(max_length=1000)

    class Meta:
        db_table = "cardio_activity"

    def __str__(self):
        return f"Distance: {self.distance}km Duration: {self.duration} Resistance/include: {self.resistance}"