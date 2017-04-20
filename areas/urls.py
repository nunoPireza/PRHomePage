from django.conf.urls import url
from . import views

app_name = 'areas'
urlpatterns = [
    url(r'^$', views.areacomum, name='areacomum'),
    url(r'^apostar/$', views.apostar, name='apostar'),
    url(r'^areapessoal/$', views.areapessoal, name='areapessoal'),
    url(r'^carregarsaldo$', views.carregarsaldo, name='carregarsaldo'),
    url(r'^editardados/$', views.editardados, name='editardados'),
    url(r'^mostardados$', views.mostrardados, name='mostrardados'),
        ]