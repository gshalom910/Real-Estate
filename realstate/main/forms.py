from django.forms import ModelForm
# from django.forms import FileField
# from django.forms import ClearableFileInput
from .models import Home,Gallery
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class HomeForm(ModelForm):
    class Meta:
        # images = FileField(widget=ClearableFileInput(attrs={'multiple': True}))
        model=Home
        fields="__all__"


class GalleryForm(ModelForm):
    class Meta:
        model=Gallery
        fields="__all__"
class Userform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','email','password1','password2']

