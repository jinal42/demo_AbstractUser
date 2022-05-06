from .models import UserProfile
from  django import forms
from django.contrib.auth.forms import UserCreationForm


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['username','email','first_name','last_name','password','password1','password2']


        

class ProfileForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ['username','email','first_name','last_name','password1','password2']
