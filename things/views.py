from django.shortcuts import render

from things.forms import ThingForm

def home(request):
    return render(request, 'home.html', {'form': ThingForm()})
