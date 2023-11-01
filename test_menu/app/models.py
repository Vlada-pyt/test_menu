from django.db import models


class Menu(models.Model):
    name = models.CharField('Название', max_length=150)
    url = models.CharField('Ссылка', max_length=280)
    description = models.TextField('Описание', max_length=300, blank=True)
    position = models.PositiveIntegerField('Позиция', default=1)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('position',)
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'


class MenuItem(models.Model):
    name = models.CharField(
        'Название пункта меню', max_length=50, unique=True)
    description = models.TextField(
        'Описание', max_length=300, blank=True,
        url=models.CharField(verbose_name='URL-адрес стороннего ресурса',
                             help_text=('Указывается для перехода на ресурс',), max_length=50, blank=True)),
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True),
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_items')

    class Meta:
        ordering = ['id']
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return self.name
