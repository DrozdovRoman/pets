from django.db import models
from django.db.models.constraints import UniqueConstraint


class AnimalClass(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Класс животного')
    description = models.TextField(
        verbose_name='Описание',
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы животных'

    def __str__(self):
        return self.name


class Breed(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Порода')
    animal_class = models.ForeignKey(AnimalClass, on_delete=models.CASCADE)
    description = models.TextField(
        verbose_name='Описание',
    )
    origin = models.CharField(max_length=100)
    average_weight = models.PositiveIntegerField()
    lifespan = models.PositiveIntegerField()
    lifespan_unit = models.CharField(
        max_length=20,
    )
    temperament = models.CharField(max_length=100)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=('name', 'animal_class'),
                name='Данная порода уже была добавлена',
            )
        ]
        ordering = ('name', 'animal_class',)
        verbose_name = 'Породу'
        verbose_name_plural = 'Породы'

    def __str__(self):
        return self.name