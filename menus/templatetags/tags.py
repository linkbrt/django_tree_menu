from django.template import Library
from menus.models import Menu


register = Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, slug):
    menu = Menu.objects.get(slug=slug)
    return {
        'menu': menu,
        'current_path': context['request'].get_full_path(),
    }
