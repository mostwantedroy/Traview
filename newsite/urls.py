from django.urls import path

from . import views

app_name = 'newsite'

urlpatterns = [
    path('', views.poster, name = 'main'),
    path('browse/',views.browse, name = 'browse')
]