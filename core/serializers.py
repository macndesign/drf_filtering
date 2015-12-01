from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Category, ExternalCategory, Association


class ExternalCategorySerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        external_category = ExternalCategory(**validated_data)
        try:
            category = Category.objects.get(name__in=validated_data['name'].split())
            external_category.save()
            association = Association(category=category, external_category=external_category)
            association.save()
        except Category.DoesNotExist:
            try:
                category = Category.objects.get(name__icontains=validated_data['name'])
                external_category.save()
                association = Association(category=category, external_category=external_category)
                association.save()
            except Category.DoesNotExist:
                return external_category
        return external_category

    class Meta:
        model = ExternalCategory


class AssociationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Association


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
