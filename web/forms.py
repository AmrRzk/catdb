from django import forms
from .models import Human, Cat, Breed, Home


class HumanForm(forms.ModelForm):
    birth_date = forms.DateField(label='Birth Date', widget=forms.DateInput(
        attrs={'placeholder': 'yyyy-mm-dd'}))

    class Meta:
        model = Human
        fields = ['name', 'gender', 'birth_date', 'description', 'home']


class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = ['name', 'address', 'house_type']


class CatForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = ['name', 'gender', 'birth_date',
                  'description', 'breed', 'owner']


class BreedForm(forms.ModelForm):
    class Meta:
        model = Breed
        fields = ['name', 'origin', 'description']
