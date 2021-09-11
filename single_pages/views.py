from django.shortcuts import render
from .models import Lang


# Create your views here.
def index(request):
    return render(
        request,
        'single_pages/index.html'
    )

def generic(request):
    return render(
        request,
        'single_pages/generic.html'
    )

#def lang_view(request):
#    langs = Lang.objects.all()
#    context = {
#        "langs": langs
#    }
#    return render(request, 'single_pages/lang.html', context) #