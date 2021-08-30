from datetime import date
from django.forms import ModelForm, DateInput, TextInput
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import  User
from .models import Car



''' add special configuration to help validate the form'''
class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'type': TextInput(attrs={"type": "text"}),
            'model': TextInput(attrs={"type": "text"}),
            'year': TextInput(attrs={"type": "text"})
        }

    def clean_date(self):
        d = self.cleaned_data.get("year")
        if d > date.today():
            raise ValidationError("year cannot be in the past")
        return d


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
