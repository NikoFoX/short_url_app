from django.urls import path
from . import views

app_name = "urlshortapp"
urlpatterns = [
    path('', views.index_view, name='index'),
    path('shorted', views.short_url_display_view, name='shorted'),
]
