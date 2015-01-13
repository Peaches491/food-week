from django.contrib import admin
from recipes.models import Recipe, Ingredient, LineItem, Unit


class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'short_description', 'line_items', 'details']}),
        ('Date information', {'fields': ['add_date']}),
    ]
    list_display = ('name','add_date', 'was_added_recently')


class IngredientAdmin(admin.ModelAdmin):
    pass
    #list_display = ('full_name',)


class UnitAdmin(admin.ModelAdmin):
    pass


class LineItemAdmin(admin.ModelAdmin):
    list_display = ('full_name',)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(LineItem, LineItemAdmin)
admin.site.register(Unit, UnitAdmin)