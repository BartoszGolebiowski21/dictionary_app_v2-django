from .models import Word

def set_number_of_reps(number):
    words = Word.objects.all()
    for word in words:
        word.remaining_repetitions = number
        word.save()
