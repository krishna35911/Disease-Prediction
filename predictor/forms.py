from django import forms
from .models import *


class BreastCancerForm(forms.Form):

    radius = forms.FloatField(label='Mean Radius', min_value=0, max_value=300, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    texture = forms.FloatField(label='Mean Texture', min_value=0, max_value=300, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    perimeter = forms.FloatField(label='Mean Perimeter', min_value=0, max_value=300, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    area = forms.FloatField(label='Mean Area', min_value=0, max_value=2000, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    smoothness = forms.FloatField(label='Mean Smoothness', min_value=0, max_value=300, widget=forms.NumberInput(attrs={'class': 'form-control'}))


class DiabetesForm(forms.Form):

    pregnancies = forms.FloatField(label='Pregnancies', min_value=0, max_value=400, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    glucose = forms.FloatField(label='Glucose', min_value=0, max_value=400, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    bloodpressure = forms.FloatField(label='Blood Pressure', min_value=0, max_value=400, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    skinthickness = forms.FloatField(label='Skin Thickness', min_value=0, max_value=400, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    insulin = forms.FloatField(label='Insulin', min_value=0, max_value=400, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    bmi = forms.FloatField(label='BMI', min_value=0, max_value=400, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    pedigree = forms.FloatField(label='Pedigree', min_value=0, max_value=400, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    age = forms.FloatField(label='Age', min_value=0, max_value=400, widget=forms.NumberInput(attrs={'class': 'form-control'}))


class HeartDiseaseForm(forms.Form):

    age = forms.FloatField(label='Age', min_value=0, max_value=100, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    sex = forms.FloatField(label='Sex', min_value=0, max_value=300, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    cp = forms.FloatField(label='CP', min_value=0, max_value=300, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    trestbps = forms.FloatField(label='TRESTBPS', min_value=0, max_value=300, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    chol = forms.FloatField(label='CHOL', min_value=0, max_value=300, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    fbs = forms.FloatField(label='FBS', min_value=0, max_value=300, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    restecg = forms.FloatField(label='RESTECG', min_value=0, max_value=300, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    thalach = forms.FloatField(label='THALACH', min_value=0, max_value=300, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    exang = forms.FloatField(label='EXANG', min_value=0, max_value=300, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    oldpeak = forms.FloatField(label='OLDPEAK', min_value=0, max_value=300, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    slope = forms.FloatField(label='SLOPE', min_value=0, max_value=300, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    ca = forms.FloatField(label='CA', min_value=0, max_value=300, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    thal = forms.FloatField(label='THAL', min_value=0, max_value=300, widget=forms.NumberInput(attrs={'class': 'form-control'}))


class regform(forms.Form):
    class Meta:
        model=reg
        fields=('name','age','add','email','psw')
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'add':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'psw':forms.TextInput(attrs={'class':'form-control'}),
            
        }
        
class docform(forms.Form):
    class Meta:
        model=doctor
        fields=('name','hos','spcl','place','mobile')
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'hos':forms.TextInput(attrs={'class':'form-control'}),
            'spcl':forms.TextInput(attrs={'class':'form-control'}),
            'place':forms.TextInput(attrs={'class':'form-control'}),
            'mobile':forms.TextInput(attrs={'class':'form-control'}),
            
        }        

class resultform(forms.Form):
    class Meta:
        model=resmodel
        fields=('name','disease')
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'disease':forms.TextInput(attrs={'class':'form-control'}),
            
        }
        
class predictForm(forms.Form):
    area= forms.CharField(max_length=10000)         