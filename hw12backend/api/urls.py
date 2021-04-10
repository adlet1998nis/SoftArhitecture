from django.urls import path

from . import views

urlpatterns = [
    path('get-name', views.get_name),
    path('get-surname', views.get_surname),
    path('get-id', views.get_id),
    path('get-additional-message', views.get_additional_message),
]
