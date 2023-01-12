from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


class User(AbstractUser):
    firstname = models.CharField(max_length=255, verbose_name='Имя')
    lastname = models.CharField(max_length=255, verbose_name='Фамилия')
    dadname = models.CharField(max_length=255, blank=True, null=True, verbose_name='Отчество')
    image = models.ImageField(blank=True, null=True, verbose_name='Изображение')
    age = models.DateField(blank=True, null=True, verbose_name='Год рождение')
    registerdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.firstname and self.lastname:
            return f"{self.firstname} {self.lastname}"
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Education(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(upload_to='images/educations/', blank=True, null=True, verbose_name='Изображение')
    text = models.TextField(blank=True, null=True, verbose_name='Описание')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Учебное заведение'
        verbose_name_plural = 'Учебные заведения'


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class Category(models.Model):
    title = models.CharField(max_length=123, verbose_name='Название')

    def __str__(self):
        return  self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Discipline(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True, verbose_name='Изображение')
    education = models.ForeignKey(Education, on_delete=models.CASCADE, related_name='edudisciplines', verbose_name='Учебное заведение')
    teacher = models.ManyToManyField(User, blank=True, null=True, related_name='disciplines', verbose_name='Учителя')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='catdisciplines', verbose_name='Категория')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = "Дисциплины"

# class TeachersDiscripline(models):
#     teacher = models.ForeignKey(User, on_delete=models.CASCADE)
#     discripline = models.ManyToManyRel(Discripline)


class Index(models.Model):
    discripline = models.ForeignKey(Discipline, on_delete=models.CASCADE, related_name='indexes', verbose_name='Показатель')
    bally = models.PositiveIntegerField(blank=True, default=0, verbose_name='Баллы')
    quantity = models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Колличество')
    protocol = models.CharField(max_length=150, blank=True, default='Пусто', verbose_name='Протокол')
    primechanie = models.CharField(blank=True, max_length=150, default='Пусто', verbose_name='Примечание')
    data = models.IntegerField(validators=[MinValueValidator(1984), max_value_current_year], verbose_name='Учебный год')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Учитель')

    def __str__(self):
        return f'Баллы по дисциплине {self.discripline}'

    class Meta:
        verbose_name = 'Баллы по дисциплине'
        verbose_name_plural = 'Баллы по дисциплине'
        unique_together = ['data', 'discripline', 'teacher']


class DocumentOtchet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.IntegerField(validators=[MinValueValidator(1984), max_value_current_year], verbose_name='Учебный год')
    document = models.FileField(upload_to='media/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Отчет от {self.user} за {self.data} год'

    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'
        ordering = ['-date',]