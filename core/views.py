from rest_framework import generics
from .serializers import CategorySerializer, ExternalCategorySerializer, AssociationSerializer
from .models import Category, ExternalCategory, Association


class CategoryTopLevel(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all().filter(parent__isnull=True)


class CategoryView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        qs = Category.objects.all()
        parent = self.request.query_params.get('parent', None)
        if parent:
            qs = qs.filter(parent=parent)

        return qs


class CategoryDetail(generics.RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ExternalCategoryCreateView(generics.CreateAPIView):
    serializer_class = ExternalCategorySerializer
    queryset = ExternalCategory.objects.all()


class ExternalCategoryListView(generics.ListAPIView):
    serializer_class = ExternalCategorySerializer
    queryset = ExternalCategory.objects.all()


class AssociationCreateView(generics.CreateAPIView):
    serializer_class = AssociationSerializer
    queryset = Association.objects.all()


class AssociationListView(generics.ListAPIView):
    serializer_class = AssociationSerializer
    queryset = Association.objects.all()
