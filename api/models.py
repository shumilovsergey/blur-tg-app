from django.db import models


class StendupAuthors(models.Model):
    name = models.CharField(max_length=56, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-created']
        verbose_name = "1. Стендап исполнитель"
        verbose_name_plural = "1. Стендап исполнители"

class StendaupFiles(models.Model):
    file_name = models.CharField(max_length=56, unique=True)
    author_name = models.ForeignKey(StendupAuthors, on_delete=models.PROTECT)
    file_id = models.CharField(max_length=256, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.author_name} __ {self.file_name}"
    class Meta:
        ordering = ['-created']
        verbose_name = "2. Стендап файл"
        verbose_name_plural = "2. Стендап файлы"