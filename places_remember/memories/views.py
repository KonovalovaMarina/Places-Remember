import folium as folium
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from geopy import Nominatim

from .forms import AddMemoryForm
from .models import Memory


def login(request):
    return render(request, 'login.html')


@login_required
def home(request):
    m = folium.Map(width=1250, height=750, location=[56.8334, 60.5984])
    memories = Memory.objects.filter(user=request.user)
    if memories:
        for memory in memories:
            geolocator = Nominatim(user_agent='Mozilla/5.0')
            location = geolocator.geocode(memory.location)
            folium.Marker(
                [location.latitude, location.longitude],
                popup=str(memory.title.encode("unicode_escape").decode()),
                icon=folium.Icon(color='red', icon='info-sign')
            ).add_to(m)
    map = m._repr_html_()
    return render(request, 'home.html', {'memories': memories, 'map': map})


@login_required
def add_memory(request):
    if request.method == 'POST':
        form = AddMemoryForm(request.POST)
        if form.is_valid():
            memory = form.save(commit=False)
            memory.user = request.user
            memory.save()
            return redirect('home')

    m = folium.Map(width=1250, height=750, location=[56.8334, 60.5984])._repr_html_()
    form = AddMemoryForm()
    return render(request, 'add_memory.html', {'form': form, 'map': m})


@login_required
def delete_memory(request):
    return render(request, 'delete_memory.html')
