from django.contrib import admin

from .models import *


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Category, CategoryAdmin, verbose_plural_name = "Категории")
admin.site.register(Tag, TagAdmin, verbose_plural_name = 'Тэги')
admin.site.register(Post, PostAdmin)