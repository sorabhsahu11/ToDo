from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, fields
from cloudinary.forms import CloudinaryFileField
from app.models import TaskModel, ProfileModel

class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['title', 'description', 'status']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUdateForm(forms.ModelForm):
    # dob = forms.DateInput()

    profile_pic = CloudinaryFileField(
        options = {
            'crop': 'thumb',
            'width': 200,
            'height': 200,
            'folder': 'profile_pics'
       }
    )

    class Meta:
        model = ProfileModel
        # fields = ['date_of_birth', 'profile_pic']
        fields = ['profile_pic']
