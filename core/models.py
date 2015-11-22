from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=75)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
