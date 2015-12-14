# coding: utf8
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from BarZar.models import Couleur, Biere
from BarZar.forms import inscriptionsForm, ConnexionForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

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
  bieres = Biere.objects.all()
  return render(request, 'commander.html', locals())

def inscription(request):
  if request.method == 'POST':
    form = inscriptionsForm(request.POST)

    if form.is_valid():
      pseudo = form.cleaned_data['pseudo']
      email = form.cleaned_data['email']
      pass1 = form.cleaned_data['pass1']
      
      User.objects.create_user(pseudo, email, pass1)
      user = authenticate(username=pseudo, password=pass1)
      login(request, user)
      return redirect("/")

  else:
    form = inscriptionsForm()
  return render(request, 'SignUp.html', locals())
  
def connexion(request):
  error = False

  if request.method == "POST":
    form = ConnexionForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data["username"]
      password = form.cleaned_data["password"]
      user = authenticate(username=username, password=password)
      if user:
        login(request, user)
      else:
        error = True
  else:
    form = ConnexionForm()
  return render(request, 'Login.html', locals())

def deconnexion(request):
    logout(request)
    return redirect("/")

def Contact(request):
  return render(request, 'Contact.html', locals())

def FAQ(request):
  return render(request, 'FAQ.html', locals())

def Adresse(request):
  return render(request, 'Adresse.html', locals())
