from django.conf.urls import url
from . import views

urlpatterns = [ 
  url(r'^$', views.accueil),
  url(r'^bieres/rousses$', views.bieres_rousses),
  url(r'^bieres/blondes$', views.bieres_blondes),
  url(r'^bieres/brunes$', views.bieres_brunes),
  url(r'^bieres/autres$', views.bieres_autres),
  url(r'^collaborateurs$',views.collaborateurs),
  url(r'^commander$',views.commander),
  url(r'^SignUp$',views.inscription),
  url(r'^Login$',views.connexion),
  url(r'^logout$',views.deconnexion),
  url(r'^Contact$',views.Contact),
  url(r'^FAQ$',views.FAQ), 
  url(r'^Adresse$',views.Adresse),
]
