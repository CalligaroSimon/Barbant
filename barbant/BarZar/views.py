# coding: utf8
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from BarZar.models import Couleur, Biere
from BarZar.forms import inscriptionsForm
from django.contrib.auth.models import User

def accueil(request):
  bieres = Biere.objects.filter(populaire="true");
  return render(request, 'accueil.html', locals())

def bieres_rousses(request):
  bieres = Biere.objects.filter(couleur__nom="Rousse");
  titre = "Bières Rousses";
  return render(request, 'bieres.html', locals())

def bieres_blondes(request):
  bieres = Biere.objects.filter(couleur__nom="Blonde");
  titre = "Bières Blondes";
  return render(request, 'bieres.html', locals())

def bieres_brunes(request):
  bieres = Biere.objects.filter(couleur__nom="Brune");
  titre = "Bières Brunes";
  return render(request, 'bieres.html', locals())

def bieres_autres(request):
  bieres = Biere.objects.filter(couleur__nom="Autre");
  titre = "Autres Bières";
  return render(request, 'bieres.html', locals())
  
def collaborateurs(request):
  return render(request, 'collaborateurs.html', locals())

def commander(request):
  return render(request, 'commander.html', locals())

def SignUp(request):
  if request.method == 'POST':
    form = inscriptionsForm(request.POST)

    if form.is_valid():
      pseudo = form.cleaned_data['pseudo']
      email = form.cleaned_data['email']
      pass1 = form.cleaned_data['pass1']
      
      User.objects.create_user(pseudo, email, pass1)
      return redirect("/")

  else:
    form = inscriptionsForm()
  return render(request, 'SignUp.html', locals())
  
def Login(request):
  return render(request, 'Login.html', locals())

def Contact(request):
  return render(request, 'Contact.html', locals())

def FAQ(request):
  return render(request, 'FAQ.html', locals())

def Adresse(request):
  return render(request, 'Adresse.html', locals())
