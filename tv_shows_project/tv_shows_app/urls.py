from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.new_show),
    path('shows/<int:id>', views.view_show),
    path('shows/<int:id>/edit', views.edit_show),
    path('shows/<int:id>/destroy', views.delete_show),
]
