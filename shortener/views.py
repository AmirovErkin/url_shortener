from django.shortcuts import render, redirect
from .models import URL
# Create your views here.


def index(request):
    if request.method == 'POST':
        original_url = request.POST['original_url']
        url = URL(original_url=original_url)
        url.save()
        return render(request, 'shortener/index.html', {'url': url})
    return render(request, 'shortener/index.html')

def redirect_to_original(request, shortened_url):
    url = URL.objects.get(shortened_url=shortened_url)
    url.click_count += 1
    url.save()
    return redirect(url.original_url)
