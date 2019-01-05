from django.shortcuts import render, redirect, reverse
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
    #### CONFIGURABLE!
    len = 6
    text = "" # DEBUG
    if request.method == "POST":
        # checking of the request's method
        form = UrlForm(request.POST)
        if form.is_valid():
            # if validation of form successful
            short_urls = ShortUrl.objects.all()
            submitted_url = form.cleaned_data.get('url')
            if submitted_url in list(short_urls.values_list('full_url', flat=True)):
                # if submitted URL is already in DB,
                # redirect to existing view of short url
                existing_short_url = short_urls.get(full_url=submitted_url).short_url
                text = existing_short_url
                return redirect('urlshortapp:short-url-display', short_url_url=existing_short_url)
            else:
                # submitted URL not in DB
                # randomize new short_url string
                shortened_url_available = "".join(string.ascii_uppercase + string.digits)
                while True:
                    shortened_url_string = str()
                    for _ in range(len):
                        elem = "".join(random.choice(shortened_url_available))
                        shortened_url_string = shortened_url_string + elem
                    if not shortened_url_string in list(short_urls.values_list("short_url", flat=True)):
                        break
                text = list(short_urls.values_list("short_url", flat=True))
                submitters = Submitter.objects.all()
                url_submitter = random.choice(submitters)
                # create new entry in DB
                new_short_url = ShortUrl(
                    short_url = shortened_url_string,
                    full_url = submitted_url,
                    submitter = url_submitter
                )
                new_short_url.save()
                return redirect('urlshortapp:short-url', short_url_url=new_short_url.short_url)
            #form = UrlForm()
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
    short_url_object = ShortUrl.objects.get(short_url=short_url_url)
    short_url = short_url_url
    full_url = short_url_object.full_url
    submitter = short_url_object.submitter
    context = {
        'short_url': short_url,
        'full_url': full_url,
        'submitter': submitter,
        'text': "", #debug
    }
    return render(request, 'urlshortapp/shorted.html', context)

# Site displaying the full_url site
def short_url_view(request, short_url_url):
    full_url = ShortUrl.objects.get(short_url=short_url_url).full_url
    return redirect(full_url)
