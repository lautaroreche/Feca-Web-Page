from django.contrib import admin
from django.contrib.sessions.models import Session
from feca_web_page_app.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    search_fields = ('id', 'name', 'price')


admin.site.register(Session)
admin.site.register(Product, ProductAdmin)
