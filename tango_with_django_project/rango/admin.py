from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'url']


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Popularity', {'fields': ['views', 'likes']})
    ]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)

# Register your models here.
