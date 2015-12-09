from django.shortcuts import render
from BarZar.models import Couleur, Biere

def accueil(request):
  bieres = Biere.objects.filter(populaire="true");
  return render(request, 'accueil.html', locals())

