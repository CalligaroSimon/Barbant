from django.db import models

class Couleur(models.Model):
  nom = models.CharField(max_length=100)

  def __str__(self):
    return self.nom

class Biere(models.Model):
  nom = models.CharField(max_length=100)
  description = models.TextField(null=True)
  image = models.CharField(max_length=100)
  populaire = models.BooleanField(default=False)
  couleur = models.ForeignKey('Couleur')
  prix = models.FloatField(default=4.99)

  def __str__(self):
    return self.nom

 
