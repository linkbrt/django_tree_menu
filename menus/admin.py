from django.contrib import admin

from .models import Menu, MenuCategory, MenuItem


class MenuItemInline(admin.TabularInline):
    model = MenuItem

    list_display = ['name', 'slug']
    search_fields = ['name', 'slug', 'title']

    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'menu', 'menu_id']
    search_fields = ['slug', 'name']

    prepopulated_fields = {'slug': ('name',)}
    inlines = [MenuItemInline]


class CategoryInLine(admin.TabularInline):
    model = MenuCategory

    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']


class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['slug', 'name']

    prepopulated_fields = {'slug': ('name',)}
    inlines = [CategoryInLine]


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuCategory, CategoryAdmin)
