from django.urls import path
from . import views

app_name = "urlshortapp"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('!<short_url>/', views.ShortUrlDisplayView.as_view(), name='short-url-display'),
    path('<short_url>/', views.ShortUrlView.as_view(), name='short-url'),
    path('<short_url>/submitted', views.ShortUrlSubmittedView.as_view(), name='short-url-submitted'),
]
