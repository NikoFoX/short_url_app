from django.urls import path
from . import views

app_name = "urlshortapp"
urlpatterns = [
    path('', views.short_url_form_view, name='index'),
]
