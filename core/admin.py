from django.contrib import admin

from .models import Product, Client


class ProductAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')


admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
