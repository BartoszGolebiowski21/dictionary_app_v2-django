from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.http import HttpResponseRedirect
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


# class AddWordView(View):
#     def get(self, request):
#         print("funkcja get się uruchamia")
#         form = WordForm()
#         return render(request, "dict_app/add_word.html", {'form': form})
    
#     def post(self, request):
#         print("funkcja post się uruchamia")
#         form = WordForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("add-word")
#         return render(request, "dict_app/add_word.html", {'form': form})


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


# class TestView(View):
#     def draw_word(self, request):
#         word = Word.objects.order_by('?')[1]
#         return word
    
#     def get(self, request):


def test(request):
    drawn_word = Word.objects.order_by('?')[1]
    if request.method == 'GET':
        form = TestForm(request.GET)
        if form.is_valid():
            print("Słowo z formularza jest obsługiwane")
            entered_word = form.cleaned_data["entered_word"]
            print(entered_word)
            print(drawn_word.english_translation)
            context = {
                "drawn_word": drawn_word, 
                "entered_word": entered_word, 
                "form": form
                }
            return render(request, "dict_app/test.html", context)        
    else:
        form = TestForm()
    context = {'drawn_word': drawn_word, "form": form}
    return render(request, "dict_app/test.html", context)
