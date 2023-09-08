from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.views import View
from django.urls import reverse, reverse_lazy
from django.db.models import Q

from .forms import WordForm, TestForm
from .models import Word


def index(request):
    return render(request, "dict_app/index.html")


class EntireDictionaryView(ListView):
    template_name = "dict_app/entire_dictionary.html"
    model = Word
    ordering = ["english_translation"]
    context_object_name = "words"


class AddWordView(CreateView):
    model = Word
    form_class = WordForm
    template_name = "dict_app/add_word.html"
    success_url = "entire-dictionary"


class SingleWordView(DetailView):
    template_name = "dict_app/word-detail.html"
    model = Word


class EditWordView(UpdateView):
    model = Word
    form_class = WordForm
    template_name = "dict_app/edit_word.html"

    def get_success_url(self):
        return reverse("word-detail", args=[self.get_object().id])
    

class DeleteWordView(DeleteView):
    model = Word
    template_name = "dict_app/delete_word.html"
    success_url = reverse_lazy("entire-dictionary")


def search(request):
    search_query = ""
    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")

    words = Word.objects.filter(Q(english_translation__icontains=search_query) 
                                | Q(polish_translation__icontains=search_query))
    
    context = {'words': words, 'search_query': search_query}
    return render(request, "dict_app/search.html", context)


class TestView(View):
    def get(self, request):
        form = TestForm()
        try:
            drawn_word = Word.objects.filter(remaining_repetitions__gt=0).order_by('?')[1]

            request.session['drawn_word_english'] = drawn_word.english_translation
            request.session['drawn_word_polish'] = drawn_word.polish_translation
            request.session['drawn_word_id'] = drawn_word.id

        except IndexError:
            drawn_word = None

        context = {'form': form, 'drawn_word': drawn_word}
        return render(request, "dict_app/test.html", context)
    
    def post(self, request):
        form = TestForm(request.POST)
        if form.is_valid():
            entered_word = form.cleaned_data["entered_word"]
            request.session['entered_word'] = entered_word

            return HttpResponseRedirect("/check")
        return render(request, "dict_app/test.html", {'form': form})


def check(request):
    drawn_word_english = request.session.get('drawn_word_english')
    drawn_word_polish = request.session.get('drawn_word_polish')
    entered_word = request.session.get('entered_word')
    drawn_word_id = request.session.get('drawn_word_id')

    # words = Word.objects.all()
    # print(words)
    # for word in words:
    #     word.remaining_repetitions = 0
    #     word.save()

    if entered_word == drawn_word_english:
        word = Word.objects.get(id=drawn_word_id)
        word.remaining_repetitions -= 1
        word.save()
        print(word.remaining_repetitions)

    context = {
        "drawn_word_english": drawn_word_english,
        "drawn_word_polish": drawn_word_polish,
        "entered_word": entered_word,
        }
    return render(request, "dict_app/check.html", context)

