from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="starting-page"),
    path("test", views.test, name="test"),
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
]
