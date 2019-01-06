from django.urls import path
from . import views

app_name = "urlshortapp"
urlpatterns = [
    path('', views.index_view, name='index'),
    path('!<short_url_url>/', views.short_url_display_view, name='short-url-display'),
    path('<short_url_url>/', views.short_url_view, name='short-url'),
    path('<short_url_url>/submitted', views.short_url_submitted, name='short-url-submitted'),
]
