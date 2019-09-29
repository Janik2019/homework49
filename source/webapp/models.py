from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Заголовок')
    text = models.TextField(max_length=3000,null=True, blank=True, verbose_name='Описание' )
    status = models.ForeignKey('webapp.Status', related_name='task_status', on_delete=models.PROTECT, verbose_name='Статус')
    type = models.ForeignKey('webapp.type', related_name='task_type', on_delete=models.PROTECT, verbose_name='Тип задачи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title


class Type(models.Model):
    type = models.CharField(max_length=15, verbose_name='Тип')

    def __str__(self):
        return self.type


class Status(models.Model):
    status = models.CharField(max_length=15, verbose_name='Статус')

    def __str__(self):
        return self.status