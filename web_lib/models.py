import uuid

from django.db import models
from django.core import validators
# Create your models here.


class Author(models.Model):
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ("name", "age")

    LIT_TYPES = (
        ("а", "Зарубежная"),
        ("б", "Фантастика"),
        ("в", "Фэнтези")
    )

    name = models.CharField(verbose_name="Имя автора",
                            max_length=200,
                            validators=[validators.RegexValidator(r"\D+", message="Че ты делаешь?")]
                            )
    age = models.PositiveSmallIntegerField(verbose_name="Возраст")

    email = models.EmailField(verbose_name="Электронная почта",
                              null=True, blank=True)

    lit_type = models.CharField(verbose_name="Жанр литературы",
                                max_length=50,
                                choices=LIT_TYPES, default="a")

    def __str__(self) -> str:
        return f"{self.name} -> {self.age} -> {self.email}"

    def test_hello(self):
        return "Hello World"

    
    test_hello.short_description = "Тестовая функция"


class Book(models.Model):

    class Meta:
        get_latest_by = "published"


    title = models.CharField(max_length=200, 
                             verbose_name="Название книги")
    description = models.TextField()
    amount_pages = models.IntegerField()
    published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title} \n-> {self.description}"