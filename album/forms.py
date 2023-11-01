
from django import forms
from .models import Player, Selection

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'height', 'weight', 'comment', 'photo']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }

class SelectionForm(forms.ModelForm):
    class Meta:
        model = Selection
        fields = ['name', 'shield', 'team']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'shield': forms.FileInput(attrs={'class': 'form-control'}),
            'team': forms.FileInput(attrs={'class': 'form-control'}),
        }
