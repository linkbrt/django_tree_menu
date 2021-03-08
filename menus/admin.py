from django.contrib import admin

from .models import Menu, MenuItem


class MenuItemInline(admin.TabularInline):
    model = MenuItem

    list_display = ['name', 'slug']
    search_fields = ['name', 'slug', 'title']

    prepopulated_fields = {'slug': ('name',)}


class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['slug', 'name']

    prepopulated_fields = {'slug': ('name',)}
    inlines = [MenuItemInline]


class MenuItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)