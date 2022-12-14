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
    user = CurrentUserSerializer(many=True)

    class Meta:
        model = Ad
        fields = ["id", "image", "description", "price", "title", "phone", "author_last_name", "author_first_name", "author_id"]
