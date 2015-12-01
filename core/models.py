from django.db import models


class ExternalCategory(models.Model):
    name = models.CharField(max_length=75)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=75)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    match = models.ManyToManyField(ExternalCategory, through='Association')

    def __str__(self):
        return self.name


class Association(models.Model):
    category = models.ForeignKey('Category', related_name='categories')
    external_category = models.ForeignKey('ExternalCategory', related_name='external_categories')
    match = models.BooleanField(default=False)

    def __str__(self):
        return 'Category: {}, ExternalCategory: {}, Match: {}'.format(
            self.category.name, self.external_category.name, self.match
        )
