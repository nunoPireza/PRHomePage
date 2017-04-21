from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.inicio, name='inicio'),
    url(r'^exitMenor$', views.exitMenor, name='exitMenor'),
    url(r'^homepage/$', views.homepage, name='homepage'),
    url(r'^novaconta/$', views.novaconta, name='novaconta'),
    url(r'^areacomum/$', views.areacomum, name='areacomum'),
    url(r'^admin/$', views.admin, name='admin'),
    url(r'^recuperarPass/$', views.recuperarPass, name='recuperarPass'),
    url(r'^$', views.returnHomepage, name='returnHomepage'),
    url(r'^aposta$', views.fazerAposta, name='fazerAposta'),
    url(r'^registo$', views.registo, name='registo'),
    url(r'^mandaEmail$', views.mandaEmail, name='mandaEmail'),
]
