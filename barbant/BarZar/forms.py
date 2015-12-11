#-*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User

class inscriptionsForm(forms.Form):
  pseudo = forms.CharField(label="Pseudo", max_length=100)
  email = forms.EmailField(label="Email")
  pass1 = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
  pass2 = forms.CharField(label="Retaper le mot de passe", widget=forms.PasswordInput)
  
  def clean(self):
    cleaned_data = super(inscriptionsForm, self).clean()
    pseudo = cleaned_data.get("pseudo")
    email = cleaned_data.get("email")
    pass1 = cleaned_data.get("pass1")
    pass2 = cleaned_data.get("pass2")
    
    user = User.objects.filter(username=pseudo)
    user2 = User.objects.filter(email=email)
    
    if user.exists() :
      self.add_error("pseudo", "Le pseudo est déja utiliser.")
    
    if user2.exists() :
      self.add_error("email", "L'email est déja utiliser.")
    
    if pass1 and pass2 :
      if pass1 != pass2 :
        self.add_error("pass2", "Les mots de passe doivent être indentique")
    
    return cleaned_data
