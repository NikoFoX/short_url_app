from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import UrlForm

# Create your views here.
def short_url_form_view(request):
    text= ""
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            text = "Form worked!"
    else:
        form = UrlForm()
        text= ""
    context = {
        'form': form,
        'text': text,
    }
    return render(request, 'urlshortapp/index.html', context)
