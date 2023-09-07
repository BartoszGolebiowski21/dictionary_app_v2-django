from django.db import models

class Word(models.Model):
    english_translation = models.CharField(max_length=80, unique=True)
    polish_translation = models.CharField(max_length=80)
    remaining_repetitions = models.IntegerField(default=8)
    english_pronunciation = models.CharField(max_length=80, blank=True, null=True)
    

    def __str__(self):
        return f"{self.id}: {self.english_translation} - {self.polish_translation}"
