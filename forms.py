from django.core import validators
import uuid
from django import forms
from .models import User
import string

class StudentRegistration(forms.ModelForm):

    def clean(self):
        cleaned_data=super().clean()
        pwd=cleaned_data['password']
        rpwd=cleaned_data['rpassword']
        if(pwd != rpwd):
            raise forms.ValidationError('password not match')
    def clean(self):
        cleaned_data=super().clean()
        pwd=cleaned_data['password']
        em=cleaned_data['password']
        if(len(pwd)<8):
            raise forms.ValidationError('length of password must be greater than or equal to 8')
        if(len(em)<8):
            raise forms.ValidationError('length of email must be greater than or equal to 8')


    class Meta:
        model=User
        fields=['first_name','last_name','email','uniqueid','password','rpassword']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
            'rpassword':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'uniqueid':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
        }