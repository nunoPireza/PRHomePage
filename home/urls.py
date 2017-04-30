from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.inicio, name='inicio'),
    url(r'^exitMenor$', views.exitMenor, name='exitMenor'),
    url(r'^homepage/$', views.homepage, name='homepage'),
    url(r'^admin/$', views.admin, name='admin'),
    url(r'^recuperarPass/$', views.recuperarPass, name='recuperarPass'),
    url(r'^registo$', views.registo, name='registo'),
    url(r'^novoRegisto$', views.novoRegisto, name='novoRegisto'),
    url(r'^loginpage$', views.loginpage, name='loginpage'),
    url(r'^loginview$', views.loginview, name='loginview'),
    url(r'^logoutview/$',views.logoutview, name='logoutview'),
    ]
