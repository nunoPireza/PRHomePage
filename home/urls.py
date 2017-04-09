from django.conf.urls import url
from . import views
app_name = 'home'

urlpatterns = [
    url(r'^$', views.homepage, name='home'),
    url(r'^novaconta/$', views.novaconta, name='novaconta'),
    url(r'^areacomum/$', views.areacomum, name='areacomum'),
    url(r'admin/$', views.admin, name='admin'),
    url(r'recuperarPass/$', views.recuperarPass, name='recuperarPass'),
    url(r'^$', views.returnHomepage, name='returnHomepage'),
]
