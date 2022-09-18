from django import forms

class AutoFormulario(forms.Form):
    marca = forms.CharField(max_length=50)
    modelo=forms.CharField(max_length=50)
    color=forms.CharField(max_length=50)
    año=forms.IntegerField()

class MotoFormulario(forms.Form):
    marca = forms.CharField(max_length=50)
    modelo=forms.CharField(max_length=50)
    color=forms.CharField(max_length=50)
    año=forms.IntegerField()

class AvionFormulario(forms.Form):
    modelo=forms.CharField(max_length=50)
    color=forms.CharField(max_length=50)
    año=forms.IntegerField()

class CamionFormulario(forms.Form):
    marca = forms.CharField(max_length=50)
    modelo=forms.CharField(max_length=50)
    color=forms.CharField(max_length=50)
    año=forms.IntegerField()