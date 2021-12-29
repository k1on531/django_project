from django.db import models
from django.contrib.auth.models import User


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    # первым параметр передается строкой, если класс объявлен после первичного класса, или ссылкой если объявлен ДО
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']


class AdvUser(models.Model):
    """
    Доп. сведения о зареганном пользователе
    связь 1к1
    """
    is_activated = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Spare(models.Model):
    """
    связь многие ко многим (ведомая)
    """
    name = models.CharField(max_length=30)


class Machine(models.Model):
    """
    связь многие ко многим (ведущая)
    """
    name = models.CharField(max_length=30)
    spares = models.ManyToManyField(Spare)
