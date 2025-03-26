from django import forms
from .models import Practica
class PracticaForm(forms.ModelForm):
    class Meta:
        model = Practica
        fields = ['nombre','email','comentarios']
# Compare this snippet from Practica1/views.py:
# from django.shortcuts import render

        