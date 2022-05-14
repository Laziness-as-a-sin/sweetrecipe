from django.db import models


class Dessert(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название десерта")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    ingredients = models.TextField(verbose_name="Ингредиенты")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name="Фотография")
    preparation_time = models.PositiveSmallIntegerField(blank=True, verbose_name="Время подготовки")
    cooking_time = models.PositiveSmallIntegerField(blank=True, verbose_name="Время готовки")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")

    def __str__(self) -> str:
        return self.title


class Recipe(models.Model):
    recipe = models.TextField(verbose_name="Рецепт")
    image = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name="Фото")
    dessert = models.ForeignKey('Dessert', on_delete=models.CASCADE, related_name="images")

    def __str__(self) -> str:
        return f'Рецепт: {self.dessert.slug}'
    

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    desserts = models.ManyToManyField(Dessert)
    

    def __str__(self) -> str:
        return self.name
