from django.urls import path
from .import views

urlpatterns = [
    path('notes/', views.NotesList.as_view(), name='notes.lis'),
    path('notes/<int:pk>', views.NoteDetailView.as_view(), name ='notes.detail'),
    path('notes/<int:pk>/edit', views.NotesUpdateView.as_view(), name ='notes.update'),
    path('notes/<int:pk>/delete', views.NotesDeleteView.as_view(), name ='notes.delete'),
    path('notes/w', views.NotesCreateView.as_view(), name= 'notes.new'),
]