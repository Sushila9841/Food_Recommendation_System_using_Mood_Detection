from django import forms

class CameraForm(forms.Form):
    image=forms.FileField(
        widget=forms.FileInput(attrs={'accept': 'image/*', 'capture':'camera'})
    )