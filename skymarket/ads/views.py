from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets, mixins
import django_filters
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny

from .models import Ad, Comment
from .permissions import IsAdmin, IsUser
from .serializers import AdSerializer, CommentSerializer, AdDetailSerializer


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
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)

    def get_serializer_class(self):
        if self.action in ["retrieve", "create", "update", "partial_update", "destroy"]:
            return AdDetailSerializer
        else:
            return AdSerializer

    def get_permissions(self):
        permission_classes = (AllowAny,)
        if self.action == "retrieve":
            permission_classes = (AllowAny,)
        elif self.action in ["create", "update", "partial_update", "destroy"]:
            permission_classes = (IsAdmin | IsUser)
        return tuple(perm() for perm in permission_classes)

    def get_queryset(self):
        if self.action == "me":
            return Ad.objects.filter(author=self.request.user)
        return Ad.objects.all()

    @action(detail=False, methods=["get"])
    def me(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        ad = get_object_or_404(Ad, id=self.kwargs.get("ad_pk"))
        serializer.save(author=self.request.user, ad=ad)

    def get_queryset(self):
        ad = get_object_or_404(Ad, id=self.kwargs.get("ad_pk"))
        return ad.comments.all()

    def get_permissions(self):
        permission_classes = (AllowAny,)
        if self.action in ["list", "retrieve"]:
            permission_classes = (AllowAny,)
        elif self.action in ["create", "update", "partial_update", "destroy"]:
            permission_classes = (IsAdmin | IsUser)
        return tuple(perm() for perm in permission_classes)
