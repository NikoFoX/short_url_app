from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import ShortUrl, Submitter
from .forms import UrlForm
import string
import random
import bs4
import requests
import urllib3
import lxml
from lxml import html
import datetime
import time

# Create your views here.
def index_view(request):
    len = 6
    text = ""
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            short_urls = ShortUrl.objects.all()
            submitted_url = form.cleaned_data.get('url')
            # CHECK IF submitted_url IS IN short_urls!
            if submitted_url in list(short_urls.values_list('full_url', flat=True)):
                text = "Url is already in DB!"
            else:
                shortened_url_available = "".join(string.ascii_uppercase + string.digits)
                while True:
                    shortened_url_string = str()
                    for _ in range(len):
                        elem = "".join(random.choice(shortened_url_available))
                        shortened_url_string = shortened_url_string + elem
                    if not shortened_url_string in list(short_urls.values_list("short_url", flat=True)):
                        break
                text = list(ShortUrl.objects.values_list("short_url", flat=True))
                submitters = Submitter.objects.all()
                url_submitter = random.choice(submitters)
                new_short_url = ShortUrl(
                    short_url = shortened_url_string,
                    full_url = submitted_url,
                    submitter = url_submitter
                )
                new_short_url.save()

            #return HttpResponseRedirect('shorted', short_url_url)
    else:
        form = UrlForm()
        text= ""
    context = {
        'form': form,
        'text': text,
    }
    return render(request, 'urlshortapp/index.html', context)

# Site of redirection after succesfull submitting new URL
def short_url_display_view(request, short_url_url):
    text = "Url shorted!"
    context = {
        'text': text,
    }
    return render(request, 'urlshortapp/shorted.html', context)

# Site displaying the full_url site
def short_url_view(request, short_url_url):
    pass

def short_url_check_view(request, short_url_url):
    pass
