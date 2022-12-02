from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    dadname = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    age = models.DateField(blank=True, null=True)
    registerdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Education(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Учебное заведение'
        verbose_name_plural = 'Учебные заведения'


class Discripline(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True)
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    teacher = models.ManyToManyField(User, blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = "Дисциплины"

# class TeachersDiscripline(models):
#     teacher = models.ForeignKey(User, on_delete=models.CASCADE)
#     discripline = models.ManyToManyRel(Discripline)


class Index(models.Model):
    discripline = models.ForeignKey(Discripline, on_delete=models.CASCADE)
    bally = models.PositiveIntegerField(blank=True, null=True)
    quantity = models.PositiveSmallIntegerField(blank=True, null=True)
    sumball = models.PositiveIntegerField(blank=True, null=True)
    quantityfact = models.PositiveIntegerField(blank=True, null=True)
    sumballfact = models.PositiveIntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    protocol = models.CharField(max_length=150, blank=True, null=True)
    primechanie = models.CharField(blank=True, max_length=150, null=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Баллы по дисциплине {self.discripline}'

    class Meta:
        verbose_name = 'Баллы по дисциплине'
        verbose_name_plural = 'Баллы по дисциплине'
