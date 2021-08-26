from datetime import date
from django.forms import ModelForm, DateInput, TextInput
from django.core.exceptions import ValidationError

from .models import Car


class MeetingForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'type': TextInput(attrs={"type": "text"}),
            'model': TextInput(attrs={"type": "text"}),
            'year': DateInput(attrs={"type": "date"})
        }

    def clean_date(self):
        d = self.cleaned_data.get("year")
        if d > date.today():
            raise ValidationError("year cannot be in the past")
        return d
