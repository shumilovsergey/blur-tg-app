from django.db import models

# stendup
class StendupAuthors(models.Model):
    name = models.CharField(max_length=56, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['created']
        verbose_name = "1. Стендап исполнитель"
        verbose_name_plural = "1. Стендап исполнители"

class StendupFiles(models.Model):
    name = models.CharField(max_length=56)
    author_name = models.ForeignKey(StendupAuthors, on_delete=models.PROTECT)
    tg_id = models.CharField(max_length=256, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.author_name} __ {self.name}"
    class Meta:
        ordering = ['-created']
        verbose_name = "2. Стендап файл"
        verbose_name_plural = "2. Стендап файлы"

#podcast
class PodcastAuthors(models.Model):
    name = models.CharField(max_length=56, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['created']
        verbose_name = "3. Подкаст исполнитель"
        verbose_name_plural = "3. Подкаст исполнители"

class PodcastFiles(models.Model):
    name = models.CharField(max_length=56)
    author_name = models.ForeignKey(PodcastAuthors, on_delete=models.PROTECT)
    tg_id = models.CharField(max_length=256, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.author_name} __ {self.name}"
    class Meta:
        ordering = ['-created']
        verbose_name = "4. Подкаст файл"
        verbose_name_plural = "4. Подкаст файлы"

#book
class BookAuthors(models.Model):
    name = models.CharField(max_length=56, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-created']
        verbose_name = "5. Книги исполнитель"
        verbose_name_plural = "5. Книги исполнители"

class BookBooks(models.Model):
    name = models.CharField(max_length=56)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(BookAuthors, on_delete=models.PROTECT)
    def __str__(self):
        return f"{self.author} __ {self.name}"
    class Meta:
        ordering = ['-created']
        verbose_name = "6. Книги книги"
        verbose_name_plural = "6. Книги книги"

class BookFiles(models.Model):
    name = models.CharField(max_length=56)
    book = models.ForeignKey(BookBooks, on_delete=models.PROTECT)
    tg_id = models.CharField(max_length=256, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.book.author} __ {self.book} __ {self.name}"
    class Meta:
        ordering = ['created']
        verbose_name = "7. Книги файл"
        verbose_name_plural = "7. Книги файлы"