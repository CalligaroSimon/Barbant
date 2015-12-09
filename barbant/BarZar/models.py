from django.db import models

class Couleur(models.Model):
  nom = models.CharField(max_length=100)

  def __str__(self):
    return self.nom

class Biere(models.Model):
  nom = models.CharField(max_length=100)
  description = models.TextField(null=True)
  couleur = models.ForeignKey('Couleur')

  def __str__(self):
    return self.nom

 
