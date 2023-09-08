from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="starting-page"),
    path("search", views.search, name="search"),
    path("entire-dictionary", views.EntireDictionaryView.as_view(), 
         name="entire-dictionary"),
    path("add-word", views.AddWordView.as_view(), name="add-word"),
    path("word-detail/<int:pk>", views.SingleWordView.as_view(), 
         name="word-detail"),
    path("word-detail/<int:pk>/edit-word", views.EditWordView.as_view(), 
         name="edit-word"),
    path("word-detail/<int:pk>/delete-word", views.DeleteWordView.as_view(), 
         name="delete-word"),
    path("test", views.TestView.as_view(), name="test"),
    path("check", views.check, name="check"),
    path("visits_count", views.visits_count, name="visits_count"),
]
