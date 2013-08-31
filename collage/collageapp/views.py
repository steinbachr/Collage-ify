from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from collage.collageapp.models import *
from collage.collageapp.forms import PictureForm

def home(request):
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('collage.collageapp.views.home'))
    else:        
        collage = Collage(name="placeholder")    
        postcards = Postcard.generate_random(collage)
    
        return render(request, 'index.html', { 'postcards': postcards,
                                               'pic_form' : PictureForm(),
                                               'pictures' : Picture.objects.all()});

def collages_list(request):
    collages = Collage.objects.all()
    
    return render(request, 'collages.html', {'collages' : collages})
