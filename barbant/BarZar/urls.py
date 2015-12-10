from django.conf.urls import url
from . import views

urlpatterns = [ 
  url(r'^$', views.accueil),
  url(r'^bieres/rousses$', views.bieres_rousses),
  url(r'^bieres/blondes$', views.bieres_blondes),
  url(r'^bieres/brunes$', views.bieres_brunes),
]
