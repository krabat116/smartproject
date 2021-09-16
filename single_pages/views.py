from django.shortcuts import render
from .models import Jinmae, Lang


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


def genericr(request):
    jin = Jinmae.objects.all()
    context={
        'jin' :jin
    }
    return render(request, 'single_pages/genericr.html', context)



#def lang_view(request):
#    langs = Lang.objects.all()
#    context = {
#        "langs": langs
#    }
#    return render(request, 'single_pages/lang.html', context) #