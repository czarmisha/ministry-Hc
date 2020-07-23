from django.db import models
from django.contrib.auth.models import User
from slugify import slugify


class Region(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название региона')
    soato = models.IntegerField(verbose_name='СОАТО')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'


class District(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название района')
    soato = models.IntegerField(verbose_name='СОАТО')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Регион', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'


class Status(models.Model):
    name = models.CharField(max_length=100, verbose_name='Статус')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class WorkSheet(models.Model):
    SHIFOKORLAR_CHOICES = (
        ('Анестезиолог-реаниматолог', 'Анестезиолог-реаниматолог'),
        ('Инфекционист', 'Инфекционист'),
        ('Эпидемиолог', 'Эпидемиолог'),
        ('Врач-лаборант', 'Врач-лаборант'),
        ('Врач-рентгенолог', 'Врач-рентгенолог'),
        ('Бошка', 'Бошка'),
    )
    HAMSHIRALAR_CHOICES = (
        ('Реанимация хамшираси', 'Реанимация хамшираси'),
        ('Палата хамшираси', 'Палата хамшираси'),
        ('Кичик тиббиёт ходимлари', 'Кичик тиббиёт ходимлари'),
        ('Бошка', 'Бошка'),
    )
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    creating_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Оператор')
    processed_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Кто обработал', blank=True,
                                       null=True, related_name='processed_user')
    consider_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Кто рассмотрел', blank=True,
                                      null=True, related_name='consider_user')
    birth_date = models.CharField(max_length=4, verbose_name='Год рождения')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Регион', null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, verbose_name='Район', null=True)
    first_phone = models.CharField(max_length=13, verbose_name='Контактный номер №1')
    second_phone = models.CharField(max_length=13, verbose_name='Контактный номер №2')
    shifokor = models.CharField(max_length=50, choices=SHIFOKORLAR_CHOICES, verbose_name='Шифокорлар', blank=True)
    hamshira = models.CharField(max_length=50, choices=HAMSHIRALAR_CHOICES, verbose_name='Хамширалар', blank=True)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Статус заявки')
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, verbose_name='url')

    class Meta:
        verbose_name = 'Анкета'
        verbose_name_plural = 'Анкеты'

    def __str__(self):
        return f'Анкета {self.first_name} {self.last_name}'

    # def get_absolute_url(self):
    #     return reverse('category', kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name + self.last_name)
        return super(WorkSheet, self).save(*args, **kwargs)
