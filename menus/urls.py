from django.urls import path

from .views import index, show_category, show_item

urlpatterns = [
    path('', index, name='index'),
    path('<slug:slug>/', show_category, name='show_category'),
    path('<slug:category_slug>/<slug:item_slug>/', show_item, name='show_item'),
]
