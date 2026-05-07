from django.contrib import admin
from django.utils.html import format_html
from .models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'category',
        'recipe_image',
    )

    search_fields = (
        'name',
        'category',
    )

    list_filter = (
        'category',
    )

    def recipe_image(self, obj):
        return format_html(
            '<img src="{}" width="50"/>',
            obj.image.url
        )