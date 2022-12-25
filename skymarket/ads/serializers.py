from rest_framework import serializers

from ads.models import Comment, Ad
from users.serializers import CurrentUserSerializer


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["id", "image", "description", "price", "title"]


class AdDetailSerializer(serializers.ModelSerializer):
    # author = CurrentUserSerializer()
    author_id = serializers.ReadOnlyField(source="author.id")
    author_last_name = serializers.ReadOnlyField(source="author.last_name")
    author_first_name = serializers.ReadOnlyField(source="author.first_name")
    phone = serializers.ReadOnlyField(source="author.phone")

    class Meta:
        model = Ad
        fields = ["id", "image", "description", "price", "title", "author_id", "author_first_name", "author_last_name",
                  "phone"]
