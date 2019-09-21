from django.db import models

# Create your models here.


status_choices = [('active', 'Активно'), ('blocked', 'Заблокировано')]


class Book(models.Model):
    author = models.CharField(max_length=100, null=False, blank=False, verbose_name='имя автора записи')
    mail = models.EmailField(max_length=100, null=False, blank=False, verbose_name='почта автора записи')
    details = models.TextField(max_length=2000, null=False, blank=False, verbose_name='текст записи')
    status = models.CharField(max_length=50, null=False, blank=False, verbose_name='статус', default='active',
                              choices=status_choices)
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    date_change = models.DateTimeField(auto_now=True, verbose_name='дата изменения')

    def __str__(self):
        return str(self.pk)
