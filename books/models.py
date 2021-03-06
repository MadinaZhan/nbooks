from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=150, verbose_name = 'Наименование')
    content = models.TextField(blank=True, verbose_name = 'Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name = 'Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name = 'Фото', blank = True)
    is_published = models.BooleanField(default=True, verbose_name = 'Опубликовано')
    genre = models.CharField(max_length=80, verbose_name ='Жанр', blank = True)
    price = models.CharField(max_length=10, verbose_name = 'Цена')
    category = models.ForeignKey('Category', on_delete = models.PROTECT, null = True, verbose_name = 'Наименование категории')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-created_at']

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']