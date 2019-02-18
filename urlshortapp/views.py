from django.shortcuts import render, redirect, reverse
from .models import ShortUrl
from django.contrib.auth.models import User
from .forms import UrlForm
import string
import random
from django.views import generic

# index view
# def index_view(request):
#     if request.method == "POST":
#         # checking of the request's method
#         form = UrlForm(request.POST)
#         if form.is_valid():
#             # if validation of form successful
#             length = int(form.cleaned_data.get('len'))
#             short_urls = ShortUrl.objects.all()
#             submitted_url = form.cleaned_data.get('url')
#             if submitted_url in list(short_urls.values_list('full_url', flat=True)):
#                 # if submitted URL is already in DB,
#                 # redirect to existing view of short url
#                 existing_short_url = short_urls.get(full_url=submitted_url).short_url
#                 return redirect('urlshortapp:short-url-submitted', short_url=existing_short_url)
#             else:
#                 # submitted URL not in DB
#                 # randomize new short_url string
#                 shortened_url_available = "".join(string.ascii_uppercase + string.digits)
#                 while True:
#                     shortened_url_string = str()
#                     for _ in range(length):
#                         elem = "".join(random.choice(shortened_url_available))
#                         shortened_url_string = shortened_url_string + elem
#                     if shortened_url_string not in list(short_urls.values_list("short_url", flat=True)):
#                         break
#                 users = User.objects.all()
#                 url_submitter = random.choice(users)
#                 # create new entry in DB
#                 new_short_url = ShortUrl(
#                     short_url = shortened_url_string,
#                     full_url = submitted_url,
#                     submitter = url_submitter
#                 )
#                 new_short_url.save()
#                 # redirect to the created url
#                 return redirect('urlshortapp:short-url-submitted', short_url=new_short_url.short_url)
#             # form = UrlForm()
#
#     else:
#         form = UrlForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'urlshortapp/index.html', context)


class IndexView(generic.FormView):
    form_class = UrlForm
    template_name = "urlshortapp/index.html"
    success_url = '/'

    def form_valid(self, form):
        # if validation of form successful
        length = int(form.cleaned_data.get('len'))
        short_urls = ShortUrl.objects.all()
        submitted_url = form.cleaned_data.get('url')
        if submitted_url in list(short_urls.values_list('full_url', flat=True)):
            # if submitted URL is already in DB,
            # redirect to existing view of short url
            existing_short_url = short_urls.get(full_url=submitted_url).short_url
            self.success_url = existing_short_url
        else:
            # submitted URL not in DB
            # randomize new short_url string
            shortened_url_available = "".join(string.ascii_uppercase + string.digits)
            while True :
                shortened_url_string = str()
                for _ in range(length) :
                    elem = "".join(random.choice(shortened_url_available))
                    shortened_url_string = shortened_url_string + elem
                if shortened_url_string not in list(short_urls.values_list("short_url", flat=True)) :
                    break
            users = User.objects.all()
            url_submitter = random.choice(users)
            # create new entry in DB
            new_short_url = ShortUrl(
                short_url=shortened_url_string,
                full_url=submitted_url,
                submitter=url_submitter
            )
            new_short_url.save()
            # redirect to the created url
            self.success_url = new_short_url.short_url
        return redirect('urlshortapp:short-url-submitted', short_url=self.get_success_url())

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


# View displaying the full_url site

# def short_url_display_view(request, short_url_url):
#     short_url_object = ShortUrl.objects.get(short_url=short_url_url)
#     short_url = short_url_url
#     full_url = short_url_object.full_url
#     submitter = short_url_object.submitter
#     context = {
#         'short_url': short_url,
#         'full_url': full_url,
#         'submitter': submitter,
#     }
#     return render(request, 'urlshortapp/shorted.html', context)


class ShortUrlDisplayView(generic.DetailView):
    model = ShortUrl
    template_name = "urlshortapp/shorted.html"
    context_object_name = 'short_url'

    def get_object(self) :
        return ShortUrl.objects.get(short_url=self.kwargs.get("short_url"))


# Redirection to full_url

# def short_url_view(request, short_url_url):
#     full_url = ShortUrl.objects.get(short_url=short_url_url).full_url
#     return redirect(full_url)


class ShortUrlView(generic.RedirectView):
    url = '%(redirect_to)'
    permanent = True

    def get_redirect_url(self, *args, **kwargs):
        redirect_to = ShortUrl.objects.get(short_url=self.kwargs.get("short_url")).full_url
        return redirect_to


# View displaying shortened link: short_url
# def short_url_submitted(request, short_url_url):
#     host = request.get_host()
#     short_url = str(host) + "/" + str(short_url_url)
#     context = {
#         'short_url': short_url,
#         'short_url_url': short_url_url,
#     }
#     return render(request, 'urlshortapp/submitted.html', context)

class ShortUrlSubmittedView(generic.DetailView):
    model = ShortUrl
    template_name = "urlshortapp/submitted.html"
    context_object_name = 'short_url'

    def get_object(self, queryset=None):
        return ShortUrl.objects.get(short_url=self.kwargs.get("short_url"))
