
# directory/urls.py
from django.urls import path
from .views import (
    MusicianListView, MusicianCreateView, MusicianUpdateView, MusicianDeleteView,
    AlbumListView, AlbumCreateView, AlbumUpdateView, AlbumDeleteView
)

urlpatterns = [
    path('musicians/', MusicianListView.as_view(), name='musician_list'),
    path('musician/add/', MusicianCreateView.as_view(), name='musician_add'),
    path('musician/<int:pk>/edit/', MusicianUpdateView.as_view(), name='musician_edit'),
    path('musician/<int:pk>/delete/', MusicianDeleteView.as_view(), name='musician_delete'),
    
    path('albums/', AlbumListView.as_view(), name='album_list'),
    path('album/add/', AlbumCreateView.as_view(), name='album_add'),
    path('album/<int:pk>/edit/', AlbumUpdateView.as_view(), name='album_edit'),
    path('album/<int:pk>/delete/', AlbumDeleteView.as_view(), name='album_delete'),
]
