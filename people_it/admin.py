from django.contrib import admin
from .models import *

class PeopleItAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cat')
    list_display_links = ('name', )
    search_fields = ('name', 'what_did')
    prepopulated_fields = {'slug': ("name", )}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name', )
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ("name", )}

admin.site.register(PeopleIt, PeopleItAdmin)
admin.site.register(Category, CategoryAdmin)

