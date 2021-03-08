from menus.models import MenuItem
from django.shortcuts import get_object_or_404, render


def index(request):
    return render(request, 'index.html')


def show_category(request, slug):
    """category = get_object_or_404(MenuCategory, slug=slug)
    return render(request, "category.html", {
        'category': category,
        'current_path': request.get_full_path(),
    })"""
    pass


def show_item(request, category_slug, item_slug):
    item = get_object_or_404(MenuItem,
                             slug=item_slug,
                             menu__slug=category_slug)
    return render(request, 'item.html', {
        'item': item,
    })
