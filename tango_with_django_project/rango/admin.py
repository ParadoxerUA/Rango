from django.contrib import admin
from rango.models import Category, Page, UserProfile

class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'url', 'views']


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = [
        (None, {'fields': ['name', 'slug']}),
        ('Popularity', {'fields': ['views', 'likes']})
    ]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)

# Register your models here.
