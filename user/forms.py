from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Replace with your custom user model if applicable

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    gender_choices = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    gender = forms.ChoiceField(choices=gender_choices)  # Use ChoiceField for choices
    calorie_goal = forms.IntegerField()
    nutrient_goal = forms.CharField(widget=forms.Textarea)  # Use Textarea widget for multi-line input

    class Meta:
        model = User  # Ensure this is the correct model
        fields = ["email", "username", "password1", "password2"]
