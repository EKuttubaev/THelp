from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    appeal = models.TextField(max_length=255, verbose_name="Обращение")
    room = models.CharField(max_length=15, verbose_name="Номер кабинета")
    person = models.CharField(max_length=30, verbose_name="Отправитель")
    status_done = models.BooleanField(default=False)
    time_and_date = models.DateTimeField(auto_now_add=True, verbose_name="Время и дата регистрации задачи")
    ip = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return self.appeal

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


class Comment(models.Model):
    comment = models.CharField(max_length=255, verbose_name="Комментарии об исполнении")
    name = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default=None)
    timedate_of_comment = models.DateTimeField(auto_now_add=True, verbose_name="Время завершения задачи")

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
