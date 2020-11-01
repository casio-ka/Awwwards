from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from .models import Post, Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

class PostForm(forms.ModelForm):
    picture = CloudinaryField('image')

    class Meta:
        model = Post
        fields = ('picture', 'name', 'website', 'description',) 

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email')

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'country', 'prof_pic', 'bio']