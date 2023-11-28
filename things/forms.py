"""Forms of the project."""
from django import forms
from models import Thing
# Create your forms here.
class ThingForm(forms.Form):
    class Meta:
        name = forms.CharField(label="name")
        description = forms.Textarea(label="description")
        quantity = forms.NumberInput(label="quantity")

    def save(self):
        super().save(comit=False)
        thing = Thing.objects.create(
            name = self.cleaned_data.get('name'),
            description = self.cleaned_data.get('description'),
            quantity = self.cleaned_data.get('quantity'),
        )
        return thing