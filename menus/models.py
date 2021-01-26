from django.db import models


class Menu(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class MenuCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    menu = models.ForeignKey(
        Menu,
        on_delete=models.SET_NULL,
        related_name='categories',
        blank=True, null=True
    )

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return f'/{self.slug}/'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    title = models.CharField(
        max_length=255,
        blank=True, null=True
    )
    category = models.ForeignKey(
        MenuCategory,
        on_delete=models.SET_NULL,
        related_name='items',
        blank=True, null=True
    )

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return f'/{self.category.slug}/{self.slug}/'
