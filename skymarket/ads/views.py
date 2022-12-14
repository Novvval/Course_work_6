from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets
import django_filters
from .models import Ad, Comment
from .serializers import AdSerializer, CommentSerializer


class AdFilter(django_filters.rest_framework.FilterSet):
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains")

    class Meta:
        model = Ad
        fields = ("title",)


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter
    pagination_class = AdPagination
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

