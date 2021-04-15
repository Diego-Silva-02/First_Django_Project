from django.urls import path
from .views import index, contact, product


urlpatterns = [
    path('', index, name='index'),
    path('contato', contact, name='contact'),
    path('produto/<int:pk>', product, name='product'),
]

# Vai receber um argumento (no caso o pk) do tipo int