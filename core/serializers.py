from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    class Meta:
        model = Category

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('category', kwargs={'pk': obj.pk}, request=request),
            'parent': reverse('category', kwargs={'pk': obj.parent.pk}, request=request) if obj.parent else None,
            'children': reverse('categories', request=request) + '?parent={}'.format(obj.pk)
        }
