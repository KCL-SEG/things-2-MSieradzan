from django import forms
from things.models import Thing
# Create your forms here.
class ThingForm(forms.Form):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {'description': forms.Textarea(),
                   'quantity': forms.NumberInput()}