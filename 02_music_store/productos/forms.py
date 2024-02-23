from .models import Disco
from django import forms

class DiscoForm(forms.ModelForm):

    class Meta:
        model = Disco
        fields = ['album', 'band', 'price', 'image']
        widgets = {
            'album': forms.TextInput(attrs={'class':'form-control', 'placeholder':'album'}),
            'band': forms.TextInput(attrs={'class':'form-control', 'placeholder':'band'}),
            'price': forms.TextInput(attrs={'class':'form-control', 'placeholder':'price'}),
            
        }
        labels = {
            'album':'', 'band':'', 'price':'', 'image': ''
        }