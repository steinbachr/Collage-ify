from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
import json

from collage.collageapp.models import *
from collage.collageapp.forms import PictureForm

def home(request):
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('collage.collageapp.views.home'))
    else:        
        collage = Collage()    
        postcards = Postcard.generate_random(collage)
    
        return render(request, 'index.html', { 'postcards': postcards,
                                               'pic_form' : PictureForm(),
                                               'pictures' : Picture.objects.all()});

def collages_list(request):
    collages = Collage.objects.all()
    
    return render(request, 'collages.html', {'collages' : collages})


#AJAX REQUESTS
def create_collage(request):    
    #kind've hacky, but good enough for now
    request_data = json.loads(request.POST.keys()[0])
    collage_name = request_data.get('name')
    postcard_data = request_data.get('data')
    
    collage = Collage(name=collage_name)
    collage.save()
    
    #create the postcards and postcard_picture instances from the postcard_data
    for p in postcard_data:
        #strip the leading media prefix (/media/) from the url of the postcard's picture
        postcard_image = str.replace(str(p['image']), "/media/", "")
        postcard = Postcard(width=p['postcard_width'], height=p['postcard_height'], \
                            collage=collage, picture=Picture.objects.filter(src=postcard_image).get())
        postcard.save()                        
        
    return HttpResponse("this is a test")
