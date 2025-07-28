from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=255),
    url = models.CharField(max_length=255),
    named_url = models.CharField(max_length=255, null=True, blank=True)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
# Create your models here.
