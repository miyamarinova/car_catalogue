from django import forms

from MyProjectRegularExam.car.models import Car


class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['owner',]
        fields = ['type', 'model', 'year', 'image_url', 'price']

        widgets = {
            'image_url': forms.URLInput(
                attrs={'placeholder': "https://..."}
            )
        }

