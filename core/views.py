from rest_framework import generics
from .serializers import CategorySerializer
from .models import Category


class CategoryTopLevel(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all().filter(parent__isnull=True)


class CategoryView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        qs = Category.objects.all()
        parent = self.request.query_params.get('parent', None)
        if parent:
            qs = qs.all().filter(parent=parent)

        return qs


class CategoryDetail(generics.RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
