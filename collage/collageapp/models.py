from django.db import models
from django.contrib import admin
import Image
import random

class Collage(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    
    @property
    def cover_photo(self):
        first_card = self.postcards[0]
        return first_card.picture.url

class Picture(models.Model):
    src = models.ImageField(upload_to="images")

    @property
    def thumbnail(self):
        #stupid and hacky..
        SUPER_SCALE_DOWN = .1
        SCALE_DOWN = .2
        width = self.src.width
        height = self.src.height

        return {'width' : width * SCALE_DOWN if width < 1500 else width * SUPER_SCALE_DOWN,
                'height' : height * SCALE_DOWN if height < 1500 else height * SUPER_SCALE_DOWN}

class Postcard(models.Model):
    width = models.IntegerField()
    height = models.IntegerField()  
    collage = models.ForeignKey(Collage, related_name="postcards")
    picture = models.ForeignKey(Picture)
    
    @classmethod
    def possible_ratios(cls):
        '''
        constrain the possible ratios we can have so we don't get really wacky dimensions when we generate
        random postcards. IMPORTANT: Ratios are in width / height
        '''
        return (.7, 1, 1.33, 2, 3)
    
    @classmethod
    def generate_random(cls, collage):        
        '''
        generate a random number of postcards between 1 and 6 (inclusive)
        returns: the postcards we generated        
        '''
        MAX_CARDS = 6      
        MAX_WIDTH = 100 #the max width to use before scaling to aspect ratio        
        num_to_gen = random.randint(2, MAX_CARDS)
        postcards = []
        
        for i in range(0,num_to_gen):
            #pick a random aspect ratio
            ratio = random.choice(Postcard.possible_ratios())
            
            #create a random dimension using the ratio
            dimension = random.randint(50, MAX_WIDTH)
            (width, height) = (dimension * ratio, dimension)
                        
            postcards.append(Postcard(width=width, height=height, collage=collage))
            
        return postcards
         


#ADMIN REGISTER
admin.site.register(Picture)
