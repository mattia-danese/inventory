from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^addProduct$', addProduct, name='addProduct'),
    url(r'^editProduct/(?P<pk>\d+)$', editProduct, name='editProduct'),
    url(r'^deleteProduct/(?P<pk>\d+)$', deleteProduct, name='deleteProduct'),
    url(r'^graphs$', displayGraph, name = "displayGraph")

]