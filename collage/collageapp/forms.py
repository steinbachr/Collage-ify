from django.forms import ModelForm
from collage.collageapp.models import Picture

class PictureForm(ModelForm):
    class Meta:
        model = Picture
        fields = ['src']
