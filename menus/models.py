from django.db import models


class Menu(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    # items = models.ManyToManyField('MenuItem', related_name='menu')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class MenuItemChoises(models.Choices):
    ITEM = 'item'
    CATEGORY = 'category'


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    title = models.CharField(
        max_length=255,
        blank=True, null=True
    )
    type = models.CharField(
        max_length=10,
        choices=MenuItemChoises.choices, default=MenuItemChoises.ITEM
    )
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items', null=True, blank=True)
    parent = models.ForeignKey('MenuItem', on_delete=models.CASCADE, null=True, blank=True, related_name='childs')

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return f'/{self.menu.slug}/{self.slug}/'
    
    def have_childs(self):
        if self.childs.all():
            return True
        return False


