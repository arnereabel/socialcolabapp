from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:                 # 2 mimimum values for the form
        model = Room            # specify the model that you want to create a form for   here it is the Room model
        fields = '__all__'      # specify the field, this will create the form based on the model from the Room class in models.py , so its loading in the values from the class to use as submissions for the form