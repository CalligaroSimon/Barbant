from django.shortcuts import render
from BarZar.models import Couleur, Biere

def accueil(request):
  bieres = Biere.objects.filter(populaire="true");
  return render(request, 'accueil.html', locals())

def bieres_rousses(request):
  bieres = Biere.objects.filter(couleur__nom="Rousse");
  return render(request, 'bieres_rousses.html', locals())

def bieres_blondes(request):
  bieres = Biere.objects.filter(couleur__nom="Blonde");
  return render(request, 'bieres_blondes.html', locals())

def bieres_brunes(request):
  bieres = Biere.objects.filter(couleur__nom="Brune");
  return render(request, 'bieres_brunes.html', locals())

def bieres_autres(request):
  bieres = Biere.objects.filter(couleur__nom="Autre");
  return render(request, 'bieres_autres.html', locals())
  
def collaborateurs(request):
  return render(request, 'collaborateurs.html', locals())


