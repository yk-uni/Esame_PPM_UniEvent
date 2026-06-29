from django.urls import path

from . import views


urlpatterns = [

    path('', views.HomeView.as_view(), name='home'),

    path(
        'create/',
        views.create_event,
        name='create_event'
    ),

    path(
        'edit/<int:pk>/',
        views.edit_event,
        name='edit_event'
    ),

    path(
        'delete/<int:pk>/',
        views.delete_event,
        name='delete_event'
    ),
    path(
        'register/<int:pk>/',
        views.register_event,
        name='register_event'
    ),
    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),

]